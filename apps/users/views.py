from django.shortcuts import render
from django.contrib.auth import login, authenticate

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# Create your views here.
# 当我们配置url被这个view处理时，自动传入request对象

from .models import UserProfile

from django.views.generic import View
from .forms import LoginForm, RegisterForm
# captcha验证码
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

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
            return render(request, 'login.html', {
                'msg': '用户名或密码错误!'
            })
    elif request.method == 'GET':
        return render(request, 'login.html', {})


# 基于类的视图实现登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')

            user = authenticate(username=user_name, password=pass_word)

            # 认证成功返回user对象，失败返回null
            if user:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {
                    'msg': '用户名或密码错误!',
                    'login_form': login_form,
                })
        else:
            return render(request, 'login.html', {
                'login_form': login_form,
            })


# 用户注册
class RegisterView(View):
    def get(self, request):
        # print(request.build_absolute_uri())  # 地址为：  http://127.0.0.1:8000/register/
        register_form = RegisterForm()
        # 图片验证码
        # hashkey验证码生成的秘钥，image_url验证码的图片地址
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        return render(request, 'register.html', {
            'register_form': register_form,
            'hashkey': hashkey,
            'image_url': image_url,
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)

        # 图片验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")

            # 用户不为空字符串，且用户
            if user_name.strip() != '' and not UserProfile.objects.filter(email=user_name):
                 # 实例化一个user_profile对象，将前台值存入
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = user_name

                # 加密password进行保存
                user_profile.password = make_password(pass_word)
                user_profile.save()

                # 发送邮件功能待写
                return render(request, 'login.html')
            else:
                return render(request, 'register.html', {
                    'register_form': register_form,
                    'msg': '邮箱已使用！',
                    'hashkey': hashkey,
                    'image_url': image_url,
                })

        return render(request, 'register.html', {
            'register_form': register_form,
            'hashkey': hashkey,
            'image_url': image_url,
        })
