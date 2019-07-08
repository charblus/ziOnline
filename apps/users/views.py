from django.shortcuts import render
from django.contrib.auth import login, authenticate

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.
# 当我们配置url被这个view处理时，自动传入request对象

from .models import UserProfile

# 自定义登录，可使用邮箱和账号


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(
                Q(username=username) | Q(email=username))

            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password)

            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(request):
    if request.method == 'POST':
        # pass
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')

        user = authenticate(username=user_name, password=pass_word)
        # 认证成功返回user对象，失败返回null
        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {})
    elif request.method == 'GET':
        return render(request, 'login.html', {})
