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
from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter
from core.api.views.pets.pet_view import PetViewSet
from core.api.views.clinics.clinic_view import ClinicViewSet
from core.api.views.medical.medical_view import MedicalRecordViewSet, MedicationViewSet
from core.api.views.appointment.appointment_view import AppointmentViewSet

router = DefaultRouter()
router.register(r'api/pets', PetViewSet)
router.register(r'api/clinics', ClinicViewSet)
router.register(r'api/medical-records', MedicalRecordViewSet)
router.register(r'api/medications', MedicationViewSet)
router.register(r'api/appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', views.listar_pets, name='listar_pets'),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('clinica/novo/', views.criar_clinica, name='criar_clinica'),
    path('clinicas/', views.listar_clinicas, name='listar_clinicas'),
    path('consulta/novo/', views.criar_consulta, name='criar_consulta'),
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('pets/novo/', views.criar_pet, name='criar_pet'),
    path('pets/editar/<int:pet_id>/', views.editar_pet, name='editar_pet'),
    path('pets/deletar/<int:pet_id>/', views.deletar_pet, name='deletar_pet'),
    path('medicalrecords/', views.listar_medicalrecords, name='listar_medicalrecords'),
    path('medicalrecords/novo/', views.criar_medicalrecord, name='criar_medicalrecord'),
    path('medications/', views.listar_medications, name='listar_medications'),
    path('medications/novo/', views.criar_medication, name='criar_medication'),
    path('user/perfil', views.informacoes_usuario, name='informacoes_usuario'),
    path('user/admin/login', views.informacoes_admin, name='login_admin'),
    path('user/admin/dashboard', views.dashboard_admin, name='informacoes_admin'),
    path('', include(router.urls)),
]