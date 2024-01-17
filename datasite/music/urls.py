from django.contrib import admin
from django.urls import path, include
from music import views

urlpatterns = [
    path('', views.music, name='music'),
    path('header', views.header, name='header'),
    path('musicprojects', views.musicprojects, name='musicprojects'),
    path('footer', views.footer, name='footer'),
]
