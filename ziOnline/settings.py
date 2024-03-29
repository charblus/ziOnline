# -*- coding: utf-8 -*-
"""
Django settings for ziOnline project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 首先导入sys模块，然后添加apps到搜索路径，插入第0是希望它先搜索我们app下东西
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))    # 添加apps搜索路径
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2xd6_w*%be2l@foj^g_&2b&_3m$tvk_az)99kwodt@f403uawz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',
    'courses',
    'organization',
    'operation',

    'xadmin',
    'crispy_forms',
    'reversion',
    'captcha',
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

ROOT_URLCONF = 'ziOnline.urls'
AUTH_USER_MODEL = 'users.UserProfile'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'ziOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zionline',
        'USER': 'root',  # 账号
        'PASSWORD': 'root',  # 密码
        'HOST': '127.0.0.1',  # IP
        'PORT': '3306',  # 端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# LANGUAGE_CODE = 'en-us'
# 语言改为中文
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
# 时区改为上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
# 数据库存储使用时间，True时间会被存为UTC的时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 设置邮箱和用户名均可登录
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# 在标准输出中输出e-mail内容来代替通过SMTP服务发送邮件
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 实际发送邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'  # smtp地址
EMAIL_HOST_USER = '3033828051@qq.com'
EMAIL_HOST_PASSWORD = 'utqvawpexoxadddd'
EMAIL_PORT = 25  # smtp端口
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = '3033828051@qq.com'
# 可以使用这个表达形式
DEFAULT_FROM_EMAIL = 'DjangoAdmin <3033828051@qq.com>'
# 管理员站点
SERVER_EMAIL = '3033828051@qq.com'
EMAIL_FROM = 'DjangoAdmin<3033828051@qq.com>'  # 一般为登录用户，也就是=EMAIL_HOST_USER