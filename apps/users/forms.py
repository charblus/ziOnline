from django import forms


class LoginForm(forms.Form):
    # 用户名和密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
