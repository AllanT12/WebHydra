from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializer import UserSerializer


@api_view(['POST'])
def register(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response( status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Create your views here.
