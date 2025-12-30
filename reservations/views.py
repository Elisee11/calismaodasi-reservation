from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation
from rooms.models import Room

# Create your views here.
@login_required
def create_reservation(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.room = room
            reservation.save()
            messages.success(request, "Rezervasyon oluşturuldu.")
            return redirect('rooms:list') 
    else:
        form = ReservationForm()
    
    # Correction du chemin ici pour éviter l'erreur TemplateDoesNotExist
    return render(request, 'create.html', {'form': form, 'room': room})
    
    
@login_required
def my_reservations(request ):
    qs = Reservation.objects.filter(user=request.user).select_related('room').order_by('-date', '-start_time')
    return render(request, 'mine.html', {'reservations': qs})




def update_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Rezervasyon güncellendi.")
            return redirect('reservations:mine')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'create.html', {'form': form, 'room': reservation.room})

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Rezervasyon silindi.")
        return redirect('reservations:mine')
    return render(request, 'delete_reservation.html', {'reservation': reservation})

