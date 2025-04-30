from rest_framework import viewsets
from core.models import VetAppointment
from ...serializers.appointment.appointment_serializers import VetAppoinmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = VetAppointment.objects.all()
    serializer_class = VetAppoinmentSerializer