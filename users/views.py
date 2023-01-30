from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from datetime import *
import LogServices
from CacheService import CacheService
from .serializer import UserSerializer
from .models import NewUser
from django.contrib.auth.hashers import make_password
from .services import UserService


class UserAPIView(APIView):
    permission_classes = [AllowAny]

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
            LogServices.write(user.errors, 'ok')
            return Response(status=status.HTTP_201_CREATED)
        else:
            LogServices.write(user.errors, 'error at creating user')
            return JsonResponse(user.errors, status=300)

    def patch(self, request):
        token = request.auth
        user = self.service.get(token.user_id, self.Cache)
        data = UserSerializer(user, many=False)
        if data.is_valid():
            data.save()
            LogServices.write(data.errors, 'ok')
            return JsonResponse(status=202, data=data.data)
        else:
            LogServices.write(data.errors, 'error at updating user')
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        token = request.auth
        self.service.delete(token.user_id, self.Cache)
        LogServices.write('delete', 'ok')
        return Response(status=status.HTTP_202_ACCEPTED)

    def get(self, request):
        token = request.auth
        user = self.service.get(token.user_id, self.Cache)
        days = datetime.today() - user.creation_date
        if(days < user.sub.days):
            return Response(status=status.HTTP_202_ACCEPTED)


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
