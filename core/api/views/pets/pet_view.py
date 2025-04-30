from rest_framework import viewsets
from core.models import Pet
from ...serializers.pets.pet_serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer