from pathlib import Path
import os
from datetime import timedelta
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xph&n#9s(sj7m)_%$@nj@m+8^gc_st3rm*#^(#5q_)l#q#@^a*'

DEBUG = True

ALLOWED_HOSTS = ["https://inno-tim.herokuapp.com", "inno-tim.herokuapp.com"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'main.apps.MainConfig',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'inno_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'inno_back.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

GRAPHENE = {
    "SCHEMA": "main.schema.schema",
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware'
    ]
}

AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend'
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://inno-tim.netlify.app"
]

CORS_ALLOW_CREDENTIALS = True

AUTH_USER_MODEL = 'main.ExtendedUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(minutes=5),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    # "JWT_VERIFY_EXPIRATION": True,
    # 'JWT_ALLOW_REFRESH': True,
    # 'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    # 'JWT_EXPIRATION_DELTA': timedelta(minutes=15),
    # 'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=14),
}
