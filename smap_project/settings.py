"""
Django settings for smap_project project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from keyring import credentials
from firebase_admin import credentials
import firebase_admin



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(y@^qkirxh^6wd9#913ts$a!3j@!gfrnsv-lj@_%$+%$iml*k2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'smap.kidsfunyfiestasinfantiles.com',
    'www.smap.kidsfunyfiestasinfantiles.com',
    'localhost',
    '127.0.0.1',
]

# Firebase Admin SDK initialization
cred_path = os.path.join(BASE_DIR, 'credentials', 'smap-kf-firebase-adminsdk-xqq0l-dc3c83c990.json')  # Reemplaza con la ruta a tus credenciales
cred = credentials.Certificate(cred_path)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    't_app_product',
    'api',
    'api_commentary',
    'api_like',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://smap.kidsfunyfiestasinfantiles.com",
    "http://localhost:8000",
    # otros orígenes permitidos
]

ROOT_URLCONF = 'smap_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 't_app_product' / 'templates' / 'home',
            BASE_DIR / 't_app_product' / 'templates' / 'push_notificated',  # Agrega esta línea para cada directorio
            BASE_DIR / 't_app_product' / 'templates' / 'other_service',
            BASE_DIR / 't_app_product' / 'templates' / 'firebase_auth',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'smap_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smap_kf',
        'USER': 'mrgomez',
        'PASSWORD': 'Karin2100',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Definir las rutas adicionales para buscar archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / "t_app_product" / "static",
]

LOGIN_URL = '/signin'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración adicional para CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://www.smap.kidsfunyfiestasinfantiles.com'
]

CSRF_COOKIE_SECURE = True

# Asegurarse de que las cookies de sesión solo se envíen a través de HTTPS
SESSION_COOKIE_SECURE = True

# Evitar que JavaScript acceda a las cookies de sesión
SESSION_COOKIE_HTTPONLY = True

# Establecer SameSite para proteger contra ataques CSRF
SESSION_COOKIE_SAMESITE = 'Lax'  # También puede ser 'Strict' dependiendo de tus necesidades

# Opcionalmente, mantener ambas configuraciones para mayor seguridad
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expira al cerrar el navegador
SESSION_COOKIE_AGE = 1800  # Y/o expira en 30 minutos en segundos

try:
    firebase_admin.initialize_app(cred)
except ValueError:
    pass  # La aplicación de Firebase ya está inicializada

SITE_DOMAIN = 'https://www.smap.kidsfunyfiestasinfantiles.com'
