from django.contrib import admin
from django.urls import path
from .views.home_views import HomePage
from .views.login_logout_views import LoginPage, LogoutPage
from .views.signup_views import SignupPage
urlpatterns = [
    path('', SignupPage, name='signup'),
    path('register/', SignupPage, name='signup'),
    path('login/', LoginPage, name='login'),
    path('home/', HomePage, name='home'),
    path('logout/',LogoutPage,name='logout'),
]
