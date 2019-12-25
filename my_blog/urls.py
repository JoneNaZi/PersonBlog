from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.login, name='login'),
    re_path(r'^$', views.home_page),
    re_path(r'^(?P<blog_id>[0-9]+)/$', views.detail, name="blog_detail"),
]

app_name = 'my_blog'
