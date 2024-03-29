"""ziOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

import xadmin

from users.views import user_login, LoginView, RegisterView, ActiveUserView, ForgetPwdView, RestpwdView, ModifypwdView
from django.urls import include


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),  # 基于类方法实现登录,这里是调用它的方法
    path('register/', RegisterView.as_view(), name='register'),
    re_path('register/active/(?P<active_code>.*)/',
            ActiveUserView.as_view(), name='user_active'),  # 激活
    path('captcha/', include('captcha.urls')),
    path('forgetpwd/', ForgetPwdView.as_view(), name='forgetpwd'),  # 忘记密码
    re_path('forgetpwd/reset/(?P<active_code>.*)/',
            RestpwdView.as_view(), name='resetpwd'),  # 密码重置验证
    path('modify_pwd/', ModifypwdView.as_view(), name="modify_pwd"),  # 密码修改
]
