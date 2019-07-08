from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    # 用户名和密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
     # 应用验证码
    captcha = CaptchaField()  # 如果验证码错误提示是英文，可以在括号内加入 error_messages={'invalid': '验证码错误'} 




# 忘记密码表单
class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


# 重置密码form实现
class ModifyPwdForm(forms.Form):
    # 密码不能小于5位
    password1 = forms.CharField(required=True, min_length=5)
    # 密码不能小于5位
    password2 = forms.CharField(required=True, min_length=5)