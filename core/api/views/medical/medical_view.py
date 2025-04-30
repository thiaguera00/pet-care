from rest_framework import viewsets
from core.models import MedicalRecord, Medication
from ...serializers.medical.medical_serializers import MedicalRecordSerializer, MedicationSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer