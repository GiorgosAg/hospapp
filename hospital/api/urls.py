from django.urls import path, include
from .views import DoctorViewSet, PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"doctors", DoctorViewSet)
router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("", include(router.urls))
]
