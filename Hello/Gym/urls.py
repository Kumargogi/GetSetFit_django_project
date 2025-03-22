from django.contrib import admin
from django.urls import path
from Gym import views

urlpatterns = [
    path('',views.index, name='Gym'),
    path('login',views.login, name='login'),
    path('home',views.home, name='home'),
    path('bulking',views.bulking,name='bulking'),
    path('cutting',views.cutting,name='cutting'),
]
