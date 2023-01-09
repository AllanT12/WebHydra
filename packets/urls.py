from django.contrib import admin
from django.urls import path, include
from .views import *
from .services import PacketService

services = PacketService
urlpatterns = [
    path('view/', PacketAPIView.as_view()),
    path('add/', PacketAPIView.as_view()),
    path('update/', PacketAPIView.as_view()),
]
