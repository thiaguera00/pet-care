from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from core.models.medical import MedicalRecord, Medication
from core.models.appointment import VetAppointment
from core.models.pet import Pet
from django.contrib import messages

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'treatment', 'notes', 'appointment']

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'end_date', 'pet']

def listar_medicalrecords(request):
    medicalrecords = MedicalRecord.objects.all()
    return render(request, 'core/medical/listar_medicalrecords.html', {'medicalrecords': medicalrecords})

def criar_medicalrecord(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prontuário criado com sucesso!')
            return redirect('listar_medicalrecords')
    else:
        appointment = VetAppointment.objects.all()
    return render(request, 'core/medical/criar_medicalrecord.html', {'appointment': appointment})

def listar_medications(request):
    medications = Medication.objects.all()
    return render(request, 'core/medical/listar_medications.html', {'medications': medications})

def criar_medication(request):
    if request.method == 'POST':
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicação criada com sucesso!')
            return redirect('listar_medications')
    else:
        pet = Pet.objects.all()
    return render(request, 'core/medical/criar_medication.html', {'pet': pet})
