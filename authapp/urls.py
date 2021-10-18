from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from authapp import views

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),
]