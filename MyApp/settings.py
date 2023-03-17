import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ovy6ph=k&ml+dqs!0ooz0orceqg-x58bnncg)4c7_581mgulx#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','*.*']


# Application definition

SHARED_APPS = (
    'django_tenants',
    'App.Main',
    'App.Authentication',
    'School.S_School',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    # School
    'School.S_Record',
    'School.S_Teachers',
    'School.S_Students',
    'School.S_Homework',
    'School.S_Fee',
    # Teacher
    'Teacher.T_Teachers',
    'Teacher.T_Students',
    'Teacher.T_Homework',
    'Teacher.T_Attendance',
    # Student
    'Student.I_Students',
    'Student.I_Homework',
    'Student.I_Attendance',
)

INSTALLED_APPS = [
    'django_tenants',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Main
    'App.Main','App.Authentication',
    # School
    'School.S_Record','School.S_School','School.S_Teachers','School.S_Students','School.S_Homework','School.S_Fee',
    # Teacher
    'Teacher.T_Teachers','Teacher.T_Students','Teacher.T_Homework','Teacher.T_Attendance',
    # Student
    'Student.I_Students','Student.I_Homework','Student.I_Attendance',
    # Extensions
    'import_export',
]

TENANT_MODEL = "S_School.School"
TENANT_DOMAIN_MODEL = "S_School.Domain"


MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'MyApp.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'MyApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'App/Main/templates/Includes')],
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

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.core.context_processors.request',
# )

WSGI_APPLICATION = 'MyApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'comsoftsystems_sms',
        'USER': 'comsoftsystems_tabish',
        'PASSWORD': 'Tabish@abc123xyz',
        'HOST': '127.0.0.1' ,
        'PORT': '5432' ,
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

SESSION_EXPIRE_SECONDS = 1500  # 1500 seconds = 25 minutes

SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

