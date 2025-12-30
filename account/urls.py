from django.urls import path
from . import views # Importe vos fonctions vues
from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_view

urlpatterns = [
    # Utilise votre fonction login_view personnalisée (pour utiliser votre logique et messages)
    path("login/", views.login_view, name="login"),
    
    # Utilise votre fonction register_view
    path("register/", views.register_view, name="register"),
    
    # Utilise votre fonction logout_view
    path("logout/", views.logout_view, name="logout"),

    path('forgot-password/',auth_view.PasswordResetView.as_view(
        template_name="forgot_password.html",
        html_email_template_name="password_reset_email.html",
        subject_template_name="password_reset_subject.txt",
        success_url=reverse_lazy("password_reset_done")
    ),name="forgot_password"),

    path('reset-password/done/',auth_view.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"
    ),name="password_reset_done"),

    path('reset-password/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(
        template_name="reset_password.html"
    ),name="password_reset_confirm"),

    path('reset-password/complete',auth_view.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    ),name="password_reset_complete")
]

