from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer
from .models import NewUser
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def register(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        db_password = make_password(user.data.get("password"))
        NewUser.objects.filter(email=user.data.get("email")).update(password=db_password)
        return Response(status=status.HTTP_201_CREATED)
    else:
        return JsonResponse(user.errors, status=300)


# Create your views here.
