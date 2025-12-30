from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
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
    if request.method=="POST":
        email=request.POST.get('email')

        if not User.objects.filter(email=email).exists():
            messages.error(request,"Bu e-posta adresi kayıtlı değil")
            return render(request,"forgot_password.html")

        messages.success(request,f"Şifre sıfırlama bağlantısı {email} adresine gönderildi. Lütfen e-postanızı kontrol edin.")
        return render(request,"forgot_password.html")

    return render(request,"forgot_password.html")

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
