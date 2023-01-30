from django.contrib import admin
from django.urls import path, include
from .views import *
from .services import DeviceService

services = DeviceService
urlpatterns = [
    path('view/', DeviceAPIView.as_view()),
    path('add/', DeviceAPIView.as_view()),
    path('update/<int:pk>', DeviceAPIView.as_view()),
    path('delete/<int:pk>', DeviceAPIView.as_view()),
]
