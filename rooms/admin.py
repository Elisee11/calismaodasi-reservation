from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity', 'is_active')
    prepopulated_fields = {'slug': ('name',)} # Génère le slug automatiquement dans l'admin