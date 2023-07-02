import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = os.environ["DEBUG"] == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "oauth2_provider",
    "social_django",
    "drf_social_oauth2",
    "compressor",
    "snowball_main",
    "snowball_blog",
    "snowball_authentication",
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
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
            "libraries": {
                "snowball_window": "snowball_main.templatetags.snowball_window"
            },
        },
        "NAME": "django",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "drf_social_oauth2.authentication.SocialAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

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
    "social_core.backends.facebook.FacebookAppOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.apple.AppleIdAuth",
    "drf_social_oauth2.backends.DjangoOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

LOGOUT_REDIRECT_URL = "/"
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

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ["state"]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = None

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")

LOGIN_REDIRECT_URL = "/"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ALLOWED_REDIRECT_URI_SCHEMES = ["https"]

# social auth
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

# FB
SOCIAL_AUTH_FACEBOOK_KEY = os.environ["FACEBOOK_CLIENT_ID"]
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ["FACEBOOK_SECRET"]
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "id, name, email"}
SOCIAL_AUTH_FACEBOOK_API_VERSION = "17.0"

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ["GOOGLE_CLIENT_ID"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
]

# Apple
SOCIAL_AUTH_APPLE_ID_CLIENT = os.environ["APPLE_CLIENT_ID"]
SOCIAL_AUTH_APPLE_ID_TEAM = os.environ["APPLE_TEAM_ID"]
SOCIAL_AUTH_APPLE_ID_KEY = os.environ["APPLE_KEY_ID"]
SOCIAL_AUTH_APPLE_ID_SECRET = os.environ["APPLE_CERTIFICATE_KEY"]
SOCIAL_AUTH_APPLE_ID_SCOPE = ["email"]
SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME = True
