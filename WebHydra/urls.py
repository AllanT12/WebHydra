from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('packets/', include('packets.urls')),
    path('admin/', admin.site.urls),
]
