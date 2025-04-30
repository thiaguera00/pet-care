from rest_framework import viewsets
from core.models import Clinic
from ...serializers.clinics.clinic_serializers import ClinicSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer