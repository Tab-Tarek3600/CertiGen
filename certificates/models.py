from django.db import models

class CertificateRequest(models.Model):
    common_name = models.CharField(max_length=255)
    validity_days = models.IntegerField(default=365)
    key_size = models.IntegerField(choices=[(2084, '2048 bits'),(4096, '4096 bits')], default=2048)
    hash_algorithm = models.CharField(choices=[('SHA256','SHA-256'),('SHA512','SHA-512')],max_length=10, default='SHA256')
    created_at = models.DateTimeField(auto_now_add=True)
