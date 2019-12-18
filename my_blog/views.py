from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.contrib import auth


def login(request):
    return render(request, 'html/login.html')


def login_action(request):
    error_msg = "用户名或密码错误"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == 'dengzhi' and password == 'dengzhi':
            return HttpResponseRedirect('/home_page')
        else:
            return render(request, 'html/login.html', {'error_msg': error_msg})


def home_page(request):
    entries = models.Entry.objects.all()
    username = request.session.get("user", "")  # 获取浏览器session
    return render(request, "html/home_page.html", {"user": username, "entries": entries})


def detail(request, blog_id):
    entry = models.Entry.objects.get(id=blog_id)
    entry.increase_visiting()

    return render(request, 'html/detail.html', {"entry": entry})
