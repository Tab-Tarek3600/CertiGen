from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status 
from .models import CertificateRequest
from .serializers import CertuficateRequestSerializer
from .utils import generate_certificate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.parsers import JSONParser

class CertificateRequestViewSet(viewsets.ModelViewSet):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertuficateRequestSerializer
    parser_classes = [JSONParser]

    def create(self, request):
        data = request.data

        try:
            validity_days = int(data["validity_days"])
            key_size = int(data["key_size"])
        except ValueError:
            return Response({"error":"validity_days et key_size doivent etre des entier"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        if key_size not in [1024,2048,4096]:
            return Response({"error":f"Taille de cle rsa invalide {key_size}"},status=status.HTTP_400_BAD_REQUEST)

        if validity_days <= 0:
            return Response({"error":"validity_days doit etre un entier positif"}, status=status.HTTP_400_BAD_REQUEST)
        
        cert_pem, key_pem = generate_certificate(
            data["common_name"],
            validity_days,
            key_size,
            data["hash_algorithm"]
        )

        cert = CertificateRequest.objects.create(
            common_name = data["common_name"],
            validity_days = validity_days,
            key_size = key_size,
            hash_algorithm = data["hash_algorithm"],
            certificate = cert_pem,
            private_key = key_pem
        )

        return Response(CertuficateRequestSerializer(cert).data, status=status.HTTP_201_CREATED)
    
def download_certificate(request, cert_id):
    cert = get_object_or_404(CertificateRequest, id=cert_id)

    response = HttpResponse(cert.certificate, content_type='application/x-pem-file')
    response['Content-Disposition'] = f'attachment; filename="{cert.common_name}.crt"'
    return response

def home(request):
    return render(request, "index.html")

