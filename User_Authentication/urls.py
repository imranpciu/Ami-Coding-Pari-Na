from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', SignupPage, name='signup'),
    path('register/', SignupPage, name='signup'),
    path('login/', LoginPage, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/',LogoutPage,name='logout'),
]
