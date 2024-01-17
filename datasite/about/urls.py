from django.contrib import admin
from django.urls import path, include
from about import views

urlpatterns = [
    path('', views.about, name='about'),
    path('header', views.header, name='header'),
    path('contact', views.contact, name='contact'),
    path('footer', views.footer, name='footer'),
]
