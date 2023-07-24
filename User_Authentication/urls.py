from django.contrib import admin
from django.urls import path
from .views.khoj_search_views import khoj_search
from .views.login_logout_views import LoginPage, LogoutPage
from .views.signup_views import SignupPage
from .views.api_views import get_all_input_values
urlpatterns = [
    path('', SignupPage, name='signup'),
    path('register/', SignupPage, name='signup'),
    path('login/', LoginPage, name='login'),
    path('khoj_search/', khoj_search, name='khoj_search'),
    path('logout/',LogoutPage,name='logout'),
    path('api/',get_all_input_values,name='get_all_input_values'),
]
