from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('get_feed', views.get_feed, name='get_feed')
]
