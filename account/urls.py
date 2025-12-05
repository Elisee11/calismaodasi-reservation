from django.urls import path
from . import views # Importe vos fonctions vues

urlpatterns = [
    # Utilise votre fonction login_view personnalisée (pour utiliser votre logique et messages)
    path("login/", views.login_view, name="login"),
    
    # Utilise votre fonction register_view
    path("register/", views.register_view, name="register"),
    
    # Utilise votre fonction logout_view
    path("logout/", views.logout_view, name="logout"),
]