from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('/readblog', views.readblog, name='readblog'),


]