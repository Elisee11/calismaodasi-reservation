README – Django Projesi
 GRUP ADI: (all)
 GRUP ÜYELERININ ISIMLERI:
   -	Ange Elisée Parfait Gahouidi
   -	Farhia Abdirahman Hassan
    -	 Heriberto Fernandez Chale
    PROJE ADI:
        Django kullanarak çalışma odası rezervasyon sistemi için web uygulaması.

PROJE HEDEFI:

Bu projenin amacı, kullanıcı yönetimini ve çalışma odası rezervasyonunu mümkün kılan, aynı zamanda iş birliğine dayalı çalışmayı ve sorumlulukların ayrıştırılmasını uygulamaya koyan bir web uygulamasını Django framework'ü kullanarak tasarlamaktır.

GRUP ÜYESI	SORUMLU UYGULAMA(lar):
Ange Elisée Parfait Gahouidi: calismaodasi, models, admin
Farhia Abdirahman Hassan:	account
Heriberto Fernandez Chale	: room, reservation




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



