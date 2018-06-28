from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^welcome', views.welcome, name='welcome'),
    url(r'^rss', views.get_feed, name='get_feed'),
]
