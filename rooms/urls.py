from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='list'),
    path('<int:pk>/', views.room_detail, name='detail'),
]

