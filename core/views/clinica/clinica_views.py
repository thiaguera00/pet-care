from django.shortcuts import render, redirect
from core.models.clinic import Clinic
from core.models.user import User
from django.contrib import messages
from django import forms

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'phone']

def listar_clinicas(request):
    clinicas = Clinic.objects.all()
    return render(request, 'core/clinica/listar.html', {'clinicas': clinicas})

def criar_clinica(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        Clinic.objects.create(
            name=name,
            address=address,
            phone=phone
        )
        messages.success(request, 'Clinica criada com sucesso!')
        return redirect('listar_clinicas')
    
    usuarios = User.objects.all()
    return render(request, 'core/clinica/cadastro.html', {'usuarios': usuarios})
