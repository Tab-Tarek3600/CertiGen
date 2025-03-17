from django.db import models

class CertificateRequest(models.Model):
    common_name = models.CharField(max_length=255)
    validity_days = models.IntegerField(default=365)
    key_size = models.IntegerField(choices=[(2048, '2048 bits'),(4096, '4096 bits')], default=2048)
    hash_algorithm = models.CharField(choices=[('SHA256','SHA-256'),('SHA512','SHA-512')],max_length=10, default='SHA256')
    certificate = models.TextField(blank=True, null=True, default='')
    private_key = models.TextField(blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cert {self.common_name} ({self.validity_days} jours)"
