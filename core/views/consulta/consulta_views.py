from django.shortcuts import render, redirect
from core.models.appointment import VetAppointment
from core.models.pet import Pet
from core.models.user import User
from core.models.clinic import Clinic
from django.contrib import messages
from django import forms

class VetAppointmentForm(forms.ModelForm):
    class Meta:
        model = VetAppointment
        fields = ['date', 'reason', 'pet', 'user_id', 'clinic_id']

def listar_consultas(request):
    consultas = VetAppointment.objects.all()
    return render(request, 'core/consulta/listar.html', {'consultas': consultas})

def criar_consulta(request):
    if request.method == 'POST':
        form = VetAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consulta criada com sucesso!')
            return redirect('listar_consultas')
    else:
        form = VetAppointmentForm()

    pets = Pet.objects.all()
    users = User.objects.all()
    clinics = Clinic.objects.all()
    return render(request, 'core/consulta/cadastro.html', {
        'form': form,
        'pets': pets,
        'users': users,
        'clinics': clinics,
    })