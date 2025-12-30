from django.urls import path
from . import views
app_name = 'reservations'

urlpatterns = [
    path('create/<int:room_pk>/', views.create_reservation, name='create'),
    path('mine/', views.my_reservations, name='mine'),

     path('update/<int:pk>/', views.update_reservation, name='update_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]