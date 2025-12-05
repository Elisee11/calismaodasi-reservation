from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation
from rooms.models import Room

# Create your views here.
def create_reservation(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            Reservation.objects.create(
                user=request.user,
                room=room,
                date=form.cleaned_data['date'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
            )
            messages.success(request, "Rezervasyon oluşturuldu.")
            return redirect('rooms:list')
    else:
        form = ReservationForm()
    return render(request, 'create.html', {'form': form, 'room': room})

@login_required
def my_reservations(request):
    qs = Reservation.objects.filter(user=request.user).select_related('room').order_by('-date', '-start_time')
    return render(request, 'mine.html', {'reservations': qs})

