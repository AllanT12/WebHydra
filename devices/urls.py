from django.contrib import admin
from django.urls import path, include
from .views import *
from .services import DeviceService

services = DeviceService
urlpatterns = [
    path('view/', DeviceAPIView.as_view()),
    path('add/', DeviceAPIView.as_view()),
    path('update/', DeviceAPIView.as_view()),
]
