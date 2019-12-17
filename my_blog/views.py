from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth


def login(request):
    return render(request, 'html/login.html')


def login_action(request):
    error_msg = "用户名或密码错误"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == 'dengzhi' and password == 'dengzhi':
            return HttpResponseRedirect('/even_manage')
        else:
            return render(request, 'html/login.html', {'error_msg': error_msg})


def even_manage(request):
    username = request.session.get("user", "")  # 获取浏览器session
    return render(request, "html/home_page.html", {"user": username})
