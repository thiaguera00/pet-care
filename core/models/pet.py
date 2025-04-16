from django.db import models
from core.models.user import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    birthdate = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')