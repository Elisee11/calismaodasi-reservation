from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_student_id', 'room', 'date', 'start_time', 'status')
    list_filter = ('status', 'date', 'room')

    def get_student_id(self, obj):
        return obj.user.student_id
    get_student_id.short_description = "Öğrenci No"