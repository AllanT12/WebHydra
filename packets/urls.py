from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('view/', view_items),
    path('add/', add_items),
    path('update/', update_items),
]
