from django.contrib import admin
from django.urls import path, include
from .views import *
from .services import PacketService

services = PacketService
urlpatterns = [
    path('view/<int:pk>', PacketAPIView.as_view()),
    path('add/', PacketAPIView.as_view()),
    path('update/<int:pk>', PacketAPIView.as_view()),
    path('delete/<int:pk>', PacketAPIView.as_view()),
]
