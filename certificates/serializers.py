from rest_framework import serializers
from .models import CertificateRequest

class CertuficateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateRequest
        fields = '__all__'