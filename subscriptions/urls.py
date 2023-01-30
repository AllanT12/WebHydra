from django.urls import path, include
from .views import *


urlpatterns = [
    path('view/', SubscriptionAPIView.as_view()),
    path('add/', SubscriptionAPIView.as_view()),
    path('update/<int:pk>', SubscriptionAPIView.as_view()),
    path('delete/<int:pk>', SubscriptionAPIView.as_view()),
]
