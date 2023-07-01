import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = int(os.environ.get("DEBUG", 1)) == 1

if DEBUG:
    os.environ["HTTPS"] = "on"
    os.environ["SSL_CERT_FILE"] = os.path.join(BASE_DIR, "localhost.crt")
    os.environ["SSL_KEY_FILE"] = os.path.join(BASE_DIR, "localhost.key")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "compressor",
    "snowball_main",
    "snowball_blog",
    "snowball_authentication",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.apple",
    "allauth.socialaccount.providers.facebook",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "snowballwebapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [os.path.join(BASE_DIR, "jinja2_templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "environment": "snowballwebapp.jinja2.environment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.csrf",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            "libraries": {
                "snowball_window": "snowball_main.templatetags.snowball_window"
            },
        },
        "NAME": "django",
    },
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

WSGI_APPLICATION = "snowballwebapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL = "/"
LOGIN_ERROR_URL = "/"
REGISTRATION_REDIRECT_URL = "/"
REGISTRATION_ERROR_URL = "/"
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

USE_L10N = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

SITE_ID = 1

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")

LOGIN_REDIRECT_URL = "/"

SOCIALACCOUNT_ADAPTER = "snowball_authentication.adapter.SnowballSocialAccountAdapter"
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "METHOD": "oauth2",
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "APP": {
            "client_id": os.environ["GOOGLE_CLIENT_ID"],
            "secret": os.environ["GOOGLE_CLIENT_SECRET"],
            "key": os.environ["GOOGLE_API_KEY"],
            "redirect_uri": "https://www.snowballtools.xyz/accounts/google/login/callback/",
            "scope": ["profile", "email"],
            "token_url": "https://oauth2.googleapis.com/token",
            "authorize_url": "https://accounts.google.com/o/oauth2/auth",
        },
    },
    "apple": {
        "APP": {
            "client_id": os.environ["APPLE_CLIENT_ID"],
            "secret": os.environ["APPLE_SECRET"],
            "key": os.environ["APPLE_KEY_ID"],
            "team_id": os.environ["APPLE_TEAM_ID"],
            "certificate_key": os.environ["APPLE_CERTIFICATE_KEY"],
            "redirect_uri": "https://www.snowballtools.xyz/accounts/apple/login/callback/",
            "scope": ["name", "email"],
            "token_url": "https://appleid.apple.com/auth/token",
            "authorize_url": "https://appleid.apple.com/auth/authorize",
        }
    },
    "facebook": {
        "METHOD": "oauth2",
        "APP": {
            "client_id": os.environ["FACEBOOK_CLIENT_ID"],
            "secret": os.environ["FACEBOOK_SECRET"],
            "AUTH_PARAMS": {"auth_type": "reauthenticate"},
            "INIT_PARAMS": {"cookie": True},
            "EXCHANGE_TOKEN": True,
            "redirect_uri": "https://www.snowballtools.xyz/accounts/facebook/login/callback/",
            "scope": ["email"],
            "VERSION": "v17.0",
            "LOCALE_FUNC": lambda request: "en_US",
            "SDK_URL": "//connect.facebook.net/{locale}/sdk.js",
        },
    },
}
