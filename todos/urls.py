from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('details/(?P<id>\w{0,50})/$', views.details, name='details'),
    url('add', views.add, name='add'),
    url('delete/(?P<id>\w{0,50})/$', views.delete, name='delete'),
]