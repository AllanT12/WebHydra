from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('devices/', include('devices.urls')),
    path('packets/', include('packets.urls')),
    path('user/', include('users.urls')),
]
