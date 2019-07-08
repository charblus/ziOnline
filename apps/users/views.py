from django.shortcuts import render
from django.contrib.auth import login, authenticate
# Create your views here.
# 当我们配置url被这个view处理时，自动传入request对象


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
