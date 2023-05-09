from django.urls import path
from .views import my_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('my_profile', my_profile)
]