from django.urls import re_path
from . import views
from .templatetags.feed import LatestEntriesFeed

urlpatterns = [
    re_path('^$', views.login, name='login'),
    re_path(r'^$', views.home_page),
    re_path(r'^(?P<blog_id>[0-9]+)/$', views.detail, name="blog_detail"),
    re_path(r'^search/$', views.search, name="blog_search"),
    re_path(r'^category/(?P<category_id>[0-9]+)/$', views.category, name="blog_category"),
    re_path(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name="blog_tag"),
    re_path(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name="blog_archives"),
    re_path(r'^latest/feed/$', LatestEntriesFeed()),
]

app_name = 'my_blog'
