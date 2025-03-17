from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateRequestViewSet

router = DefaultRouter()
router.register(r'certificates',CertificateRequestViewSet, basename='certificate')

urlpatterns = [
    path('', include(router.urls)),
]
