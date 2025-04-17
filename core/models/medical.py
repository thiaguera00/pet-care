from django.db import models
from core.models.appointment import VetAppointment
from core.models.pet import Pet

class MedicalRecord(models.Model):
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True)
    appointment_id = models.OneToOneField(VetAppointment, on_delete=models.CASCADE, related_name='medical_record')

class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='medications')