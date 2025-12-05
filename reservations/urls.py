from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:room_pk>/', views.create_reservation, name='create'),
    path('mine/', views.my_reservations, name='mine'),
]