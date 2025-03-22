from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateRequestViewSet 
from .views import download_certificate

router = DefaultRouter()
router.register(r'certificates',CertificateRequestViewSet, basename='certificate')

urlpatterns = [
    path('', include(router.urls)),
    path('certificates/<int:cert_id>/download/', download_certificate, name='download_certificate'),
]
