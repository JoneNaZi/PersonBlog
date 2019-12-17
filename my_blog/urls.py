from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.login, name='login'),
    re_path(r'^$', views.login_action, name='login_action'),
    re_path(r'^$', views.even_manage, name='even_manage'),
]
