from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet, Clinic, VetAppointment, MedicalRecord, Medication

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(Pet)
admin.site.register(Clinic)
admin.site.register(VetAppointment)
admin.site.register(MedicalRecord)
admin.site.register(Medication)
