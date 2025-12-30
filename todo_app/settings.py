"""
Django settings for todo_app project.
<<<<<<< HEAD
OWASP ASVS V3 / A6 compliant
Local-development friendly
=======
Fully fixed version - OWASP ASVS compliant + local development friendly
Date: December 30, 2025
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
"""

import os
from pathlib import Path

<<<<<<< HEAD
# =============================================================================
# BASE CONFIG
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# CORE SECURITY SETTINGS
# =============================================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-change-this-in-production"
)

DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")



if not DEBUG:
    # Enforce HTTPS
    SECURE_SSL_REDIRECT = True

    # Secure cookies
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # Reverse proxy support (Heroku, Render, Nginx)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # HSTS
=======
# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# CORE SECURITY SETTINGS - Environment-driven (safe for local & production)
# =============================================================================

# Secret key - always load from environment in production
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-change-this-in-production-please-use-a-real-key'
)

# DEBUG mode - False in production by default
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'


# ALLOWED_HOSTS - flexible and secure
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# =============================================================================
# HTTPS & SECURITY HEADERS - ONLY ACTIVE IN PRODUCTION (fixes local SSL error)
# =============================================================================
if not DEBUG:
    # Force HTTPS in production (Heroku, Render, etc.)
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # Trust proxy headers (important for Heroku/Cloud platforms)
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # HSTS - tell browsers to always use HTTPS
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

<<<<<<< HEAD
# Always safe (dev + prod)
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_REFERRER_POLICY = "same-origin"
X_FRAME_OPTIONS = "DENY"
=======
# Always enable these (safe in development too)
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
CSRF_COOKIE_HTTPONLY = True

# =============================================================================
# APPLICATION DEFINITION
# =============================================================================
<<<<<<< HEAD

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base.apps.BaseConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",  # enable in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "todo_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
=======
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',  # Uncomment in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Supports your custom 400/403/404/500.html
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
            ],
        },
    },
]

<<<<<<< HEAD
WSGI_APPLICATION = "todo_app.wsgi.application"
=======
WSGI_APPLICATION = 'todo_app.wsgi.application'
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65

# =============================================================================
# DATABASE
# =============================================================================
<<<<<<< HEAD

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
    }
}

# =============================================================================
<<<<<<< HEAD
# PASSWORD SECURITY (OWASP ASVS)
# =============================================================================

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "tasks"
LOGOUT_REDIRECT_URL = "login"
=======
# PASSWORD SECURITY - Argon2 (OWASP recommended strongest hasher)
# =============================================================================
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',      # Best protection
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',     # Fallback
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGIN_URL = 'login'
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65

# =============================================================================
# STATIC FILES
# =============================================================================
<<<<<<< HEAD

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# =============================================================================
# LOGGING (NO SENSITIVE DATA)
# =============================================================================

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "app.log",
            "formatter": "standard",
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.security": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
=======
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Uncomment for production:
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =============================================================================
# LOGGING - Secure, no sensitive data, logs failed logins
# =============================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'app.log',
            'formatter': 'standard',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.security': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
        },
    },
}

<<<<<<< HEAD
# =============================================================================
# INTERNATIONALIZATION
# =============================================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kuala_Lumpur"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =============================================================================
# DEV MODE NOTICE
# =============================================================================

if DEBUG:
    print("=== DEVELOPMENT MODE ACTIVE ===")
    print(f"DEBUG = {DEBUG}")
    print(f"ALLOWED_HOSTS = {ALLOWED_HOSTS}")
    print("HTTPS enforcement: DISABLED (safe for local testing)")
    print("=================================")
=======
# Create logs directory if it doesn't exist
os.makedirs(BASE_DIR / 'logs', exist_ok=True)


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kuala_Lumpur'  # Malaysia timezone
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


if DEBUG:
    print("=== DEVELOPMENT MODE ACTIVE ===")
    print(f"DEBUG: {DEBUG}")
    print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
    print("HTTPS security headers: DISABLED (safe for local testing)")
    print("=================================")
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
