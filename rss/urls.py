from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_feed, name='get_feed'),
]
