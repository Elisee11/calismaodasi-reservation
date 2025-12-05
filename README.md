# django
CALISMAODASI/
├── manage.py
├── db.sqlite3
├── calismaodasi/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── img/
│   │       └── library.jpg
│   └── templates/
│       └── calismaodasi/
│           ├── base.html
│           └── home.html
├── rooms/          # Odaların yönetimi
├── reservations/   # Rezervasyon işlemleri
├── users/          # Kullanıcı yönetimi
├── notifications/  # Bildirimler

git clone https://github.com/kullanici/calismaodasi.git
cd calismaodasi

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser


🎨 Tasarım
- Framework: Bootstrap 5.3
- Özel stiller: static/css/styles.css
- Responsive navbar ve modern arayüz
- Sıcak renk paleti (turuncu, gri, beyaz)

📌 Gelecek Geliştirmeler
- Ana sayfada hero section eklenmesi
- Giriş/çıkış akışlarında kullanıcıya daha net mesajlar
- Rezervasyon bildirimlerinin eklenmesi
- Odalar için daha gerçekçi içerik ve görseller
