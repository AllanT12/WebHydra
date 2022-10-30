from django.urls import path, include
from .views import *
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', register),
    path('login/', views.obtain_auth_token)
]
