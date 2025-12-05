from django.shortcuts import render
from .models import Room

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, 'detail.html', {'room': room})

