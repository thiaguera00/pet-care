from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from core.models.medical import MedicalRecord, Medication
from django.contrib import messages

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'treatment', 'notes', 'appointment_id']

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage', 'frequency', 'start_date', 'end_date', 'pet_id']

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
        form = MedicalRecordForm()
    return render(request, 'core/medical/criar_medicalrecord.html', {'form': form})

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
        form = MedicationForm()
    return render(request, 'core/medical/criar_medication.html', {'form': form})
