from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from CacheService import CacheService
from .serializer import UserSerializer
from .models import NewUser
from django.contrib.auth.hashers import make_password
from .services import UserService
class UserAPIView(APIView):

    @inject
    def setup(self, request, my_service: UserService, Cache: CacheService , **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs
        self.Cache = Cache

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            self.service.encrypt(user=user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(user.errors, status=300)

"""
@api_view(['POST'])
def register(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        UserService.encrypt(user=user)
        return Response(status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(user.errors, status=300)
"""
