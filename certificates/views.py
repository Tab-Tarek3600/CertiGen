from rest_framework import viewsets
from .models import CertificateRequest
from .serializers import CertuficateRequestSerializer

class CertificateRequestViewSet(viewsets.ModelViewSet):
    queryset = CertificateRequest.objects.all()
    serializer_class = CertuficateRequestSerializer
