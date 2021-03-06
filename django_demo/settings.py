# coding=utf-8


"""
Django settings for django_demo project.

Generated by 'django-admin startproject' using Django 1.10b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0!*z7ffk)s&johctzc@27%q*m^^g+@ed!u(@bddcezon&(l*2y'



#===============================================================================
# 调试模型开关，开发阶段建议开启；部署阶段请关闭，关闭之后ALLOWED_HOSTS必须设置，不然无法访问
#===============================================================================
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sessionAlim',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_demo.urls'



#===============================================================================
#  session 配置
#===============================================================================
SESSION_ENGINE    = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = 'C:\django_session_tmp'




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

WSGI_APPLICATION = 'django_demo.wsgi.application'



#===============================================================================
# 数据库相关配置，以下为mysql配置
# 默认使用sqlite3
# 【sqlite3】
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#===============================================================================
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'djangodb',
        'USER'    : 'root',
        'PASSWORD': 'root',
        'HOST'    : '127.0.0.1',
        'PORT'    : '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




#===============================================================================
# 静态文件所在目录，一般我们我们只要把静态文件放在APP中的static目录下，部署时用python manage.py collectstatic 就可以把静态文件收集到STATIC_ROOT目录，
# 但有一些公共文件，这时候就可以设置STATICFILES_DIRS另外一个文件夹
#===============================================================================
STATIC_URL  = '/static/'
STATIC_ROOT = '/django-demo/static/' # 总的static目录，可以使用命令自动收集static文件
# 存放各个APP的static目录及公共的static目录
CTATICFILES_DIRS = []


































