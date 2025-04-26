"""
URL configuration for petcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', views.listar_pets, name='listar_pets'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('pets/novo/', views.criar_pet, name='criar_pet'),
    path('pets/editar/<int:pet_id>/', views.editar_pet, name='editar_pet'),
    path('pets/deletar/<int:pet_id>/', views.deletar_pet, name='deletar_pet'),
    path('medicalrecords/', views.listar_medicalrecords, name='listar_medicalrecords'),
    path('medicalrecords/novo/', views.criar_medicalrecord, name='criar_medicalrecord'),
    path('medications/', views.listar_medications, name='listar_medications'),
    path('medications/novo/', views.criar_medication, name='criar_medication'),
]
