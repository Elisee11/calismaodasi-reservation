from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'student_id', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations Étudiant', {'fields': ('student_id',)}),
    )