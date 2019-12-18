from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.login),
    re_path(r'^$', views.login_action),
    re_path(r'^$', views.home_page),
    re_path(r'^$', views.detail, name="blog_detail"),
]

app_name = 'my_blog'
