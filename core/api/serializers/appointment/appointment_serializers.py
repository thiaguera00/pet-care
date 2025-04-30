from rest_framework import serializers
from core.models import VetAppointment

class VetAppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetAppointment
        fields = '__all__'