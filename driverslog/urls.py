'''
Created on Feb 1, 2015

@author: zking
'''
from django.conf.urls import patterns, url
from driverslog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^trips/$', views.trips, name='trips'),
    url(r'^trips/(?P<trip_id>\d+)/$', views.trip, name='trip'),
)