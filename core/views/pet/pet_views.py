from django.shortcuts import render, get_object_or_404, redirect
from core.models.pet import Pet
from core.models.user import User
from django.contrib import messages
from django import forms

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'birthdate', 'user_id']

def listar_pets(request):
    pets = Pet.objects.all()
    return render(request, 'core/pets/listar.html', {'pets': pets})

def criar_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        breed = request.POST.get('breed')
        birthdate = request.POST.get('birthdate')
        user_id = request.POST.get('user_id')

        owner = User.objects.get(id=user_id)
        Pet.objects.create(
            name=name,
            species=species,
            breed=breed,
            birthdate=birthdate,
            user_id=owner
        )
        messages.success(request, 'Pet criado com sucesso!')
        return redirect('listar_pets')
    
    usuarios = User.objects.all()
    print(usuarios) 
    return render(request, 'core/pets/cadastro.html', {'usuarios': usuarios})

def editar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet atualizado com sucesso!')
            return redirect('listar_pets')
    else:
        form = PetForm(instance=pet)
    return render(request, 'core/pets/editar.html', {'form': form, 'titulo': 'Editar Pet'})

def deletar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.delete()
    messages.success(request, 'Pet removido com sucesso!')
    return redirect('listar_pets')
