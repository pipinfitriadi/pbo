# inventory_management/settings.py

DEBUG = False  # Atur ke True untuk pengembangan

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Tambahkan domain Anda jika ada

# Pengaturan lainnya...
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
# inventory_management/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Contoh menggunakan Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
# inventory_management/settings.py
EMAIL_HOST_PASSWORD = 'your_password'  # Kata sandi email Anda