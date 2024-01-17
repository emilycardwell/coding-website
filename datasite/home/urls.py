from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('header', views.header, name='header'),
    path('blurb', views.blurb, name='blurb'),
    path('projects', views.projects, name='projects'),
    path('footer', views.footer, name='footer'),
]
