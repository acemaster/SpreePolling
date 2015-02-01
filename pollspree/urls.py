from django.conf.urls import patterns, url
from pollspree import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))