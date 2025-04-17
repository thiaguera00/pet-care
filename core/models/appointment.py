from django.db import models
from core.models.user import User
from core.models.pet import Pet
from core.models.clinic import Clinic

class VetAppointment(models.Model):
    date = models.DateTimeField()
    reason = models.TextField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='appointments')