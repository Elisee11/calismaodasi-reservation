from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
User = get_user_model()


def register_view(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        password2=request.POST.get("password2")
        firstname=request.POST.get("firstname","")
        lastname=request.POST.get("lastname","")
        email=request.POST.get("email")
        studentid=request.POST.get("studentid")

        

        if password!=password2:
            messages.warning(request,"sifre yanlis!")
            return render(request,"register.html")
        if User.objects.filter(username=username).exists():
            messages.warning(request,"bu kullanici zaten var ! ")
            return render(request,"register.html")
        
        newuser=User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=firstname,
            last_name=lastname,
            student_id=studentid,
        )
        newuser.save()
        messages.success(request, "Kayıt işlemi başarıyla tamamlandı! Artık giriş yapabilirsiniz.")
        return redirect("login")

    return render(request,"register.html")

def logout_view(request):
    logout(request)
    messages.success(request, "cikis yaptiniz!")
    return redirect('login')

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"baglanti basarili.")
            return redirect('home')  
        else:
            messages.error(request,"Kullanıcı bulunamadı ")
            return render(request,'login.html')

    return render(request,"login.html")

def forgot_password_view(request):
    User = get_user_model()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        users = User.objects.filter(email=email)

        if users.exists():
            # Stocker l'email dans la session pour l'étape suivante
            request.session['reset_email'] = email
            messages.success(
                request,
                "✓ Şifre sıfırlama bağlantısı e-posta adresinize gönderildi."
            )
            # Rediriger vers la page de réinitialisation
            return redirect('accounts:reset_password')
        else:
            messages.error(
                request,
                "✗ Bu e-posta adresi kayıtlı değil."
            )
            return redirect('accounts:forgot_password')

    return render(request, 'forgot_password.html')

def reset_password_view(request):
    if request.method=="POST":
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request,"Girdiğiniz şifreler uyuşmuyor")
            return render(request,"reset_password.html")

        if len(password) < 8:
            messages.error(request,"Şifre en az 8 karakter olmalıdır")
            return render(request,"reset_password.html")

        messages.success(request,"Şifreniz başarıyla güncellendi. Yeni şifrenizle giriş yapabilirsiniz.")
        return redirect('login')

    return render(request,"reset_password.html")


def confirm_reset_password(request, uidb64=None, token=None):
    """Confirme et change le mot de passe"""
    
    if request.user.is_authenticated:
        return redirect('home')
    
    User = get_user_model()
    
    # Décoder le token
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    
    # Vérifier si le lien est valide
    if user is None or not default_token_generator.check_token(user, token):
        messages.error(request, "Lien invalide ou expiré!")
        return redirect('forgot_password')
    
    if request.method == 'POST':
        # Récupérer les champs avec les noms Django par défaut
        password = request.POST.get('new_password1')
        confirm = request.POST.get('new_password2')
        
        print(f"DEBUG - Password: {password}")
        print(f"DEBUG - Confirm: {confirm}")
        
        # Validation
        if not password or not confirm:
            messages.error(request, "Veuillez remplir les deux champs!")
        elif password != confirm:
            messages.error(request, "Les mots de passe ne correspondent pas!")
        elif len(password) < 6:
            messages.error(request, "Le mot de passe doit avoir au moins 6 caractères!")
        else:
            # Enregistrer le nouveau mot de passe
            user.set_password(password)
            user.save()
            
            messages.success(request, "✅ Mot de passe changé avec succès! Vous pouvez maintenant vous connecter.")
            return redirect('login')
        
        # Si validation échoue, re-render avec les erreurs
        return render(request, 'reset_password.html', {
            'uidb64': uidb64,
            'token': token,
            'validlink': True,
            'form': None  # Vous pouvez créer un formulaire si besoin
        })
    
    # GET request
    return render(request, 'reset_password.html', {
        'uidb64': uidb64,
        'token': token,
        'validlink': True,
        'form': None
    })