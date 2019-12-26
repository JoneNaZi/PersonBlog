from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.login, name='login'),
    re_path(r'^$', views.home_page),
    re_path(r'^(?P<blog_id>[0-9]+)/$', views.detail, name="blog_detail"),
    re_path(r'^search/$', views.search, name="blog_search"),
    re_path(r'^category/(?P<category_id>[0-9]+)/$', views.category, name="blog_category"),
]

app_name = 'my_blog'
