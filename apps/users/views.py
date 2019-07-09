from django.shortcuts import render
from django.contrib.auth import login, authenticate

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponseRedirect 
# Create your views here.
# 当我们配置url被这个view处理时，自动传入request对象

from .models import UserProfile, EmailVerifyRecord

from django.views.generic import View
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
# captcha验证码
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

# django自带的类库，加密解密
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
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
                # return render(request, 'index.html')
                return HttpResponseRedirect("/xadmin/") 
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
                # 默认激活状态True，需要改为False
                user_profile.is_active = False
                user_profile.save()

                # 发送注册激活邮件
                send_register_email(request_uri=request.build_absolute_uri(
                ), email=user_name, send_type='register')

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


# 激活用户
class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询验证码是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)

        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html', {
                    'msg': '激活用户成功'
                })

        else:
            register_form = RegisterForm()
            hashkey = CaptchaStore.generate_key()
            image_url = captcha_image_url(hashkey)
            return render(request, 'register.html', {
                "msg": "您的激活链接无效",
                'register_form': register_form,
                'hashkey': hashkey,
                'image_url': image_url,
            })


# 忘记密码视图
class ForgetPwdView(View):
    def get(self, request):
        # print(request.build_absolute_uri())
        forgetpwd_form = ForgetPwdForm()
        # 图片验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        return render(request, 'forgetpwd.html', {
            'forgetpwd_form': forgetpwd_form,
            'hashkey': hashkey,
            'image_url': image_url,
        })

    def post(self, request):
        forgetpwd_form = ForgetPwdForm(request.POST)
        # 图片验证码
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)

        if forgetpwd_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                # 如果邮箱是注册过的，就发送改密邮件，然后跳回登录页面
                send_register_email(
                    request_uri=request.build_absolute_uri(), email=email, send_type='forget')

                return render(request, 'login.html', {
                    'msg': '重置密码邮件已发送,请注意查收',
                })
            else:
                return render(request, 'forgetpwd.html', {
                    'forgetpwd_form': forgetpwd_form,
                    'hashkey': hashkey,
                    'image_url': image_url,
                    'msg': '邮箱未注册，请检查是否输入错误'
                })
        else:
            return render(request, 'forgetpwd.html', {
                'forgetpwd_form': forgetpwd_form,
                'hashkey': hashkey,
                'image_url': image_url,
            })


# 重置密码
class RestpwdView(View):
    def get(self, request, active_code):
        # 查询验证码是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)

        if all_record:
            for record in all_record:
                email = record.email

                return render(request, 'pwdreset.html', {
                    'email': email
                })
        else:
            forgetpwd_form = ForgetPwdForm()
            hashkey = CaptchaStore.generate_key()
            image_url = captcha_image_url(hashkey)

            return render(request, 'forgetpwd.html', {
                'forgetpwd_form': forgetpwd_form,
                "msg": "您的重置链接无效",
                'hashkey': hashkey,
                'image_url': image_url,
            })


# 修改密码
class ModifypwdView(View):
    def post(self, request):
        modifypwd_form = ModifyPwdForm(request.POST)
        if modifypwd_form.is_valid():
            pwd1 = request.POST.get("password", "")
            pwd2 = request.POST.get("re_password", "")
            email = request.POST.get("email", "")
            # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return render(request, "pwdreset.html", {
                    "email": email,
                    "msg": "密码不一致",
                    'modifypwd_form': modifypwd_form,
                })
            # 如果密码一致
            user = UserProfile.objects.get(email=email)
            # 加密成密文
            user.password = make_password(pwd2)
            # save保存到数据库
            user.save()
            return render(request, "login.html", {"msg": "密码修改成功，请登录"})
        else:
            email = request.POST.get("email", "")
            return render(request, 'pwdreset.html', {
                'email': email,
                'modifypwd_form': modifypwd_form,
            })
