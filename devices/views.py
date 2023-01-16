from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from CacheService import CacheService
from .serializer import DeviceSerializer
from .services import DeviceService


class DeviceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @inject
    def setup(self, request, my_service: DeviceService, Cache: CacheService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs
        self.Cache = Cache

    def get(self, request):
        devices = self.service.get_all(self.Cache)
        if devices:
            data = DeviceSerializer(devices, many=True)
            return JsonResponse(status=202, data=data.data, safe=False)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        device = DeviceSerializer(data=request.data)
        if device.is_valid():
            device.save()
            self.Cache.set(key=device.data.get('deivceid'), data=device)
            return JsonResponse(device.errors, status=202)
        else:
            return JsonResponse(device.errors, status=400)

    def patch(self, request, pk):
        device = self.service.get(nr=pk, Cache=self.Cache)
        data = DeviceSerializer(instance=device, data=request.data)
        if data.is_valid():
            data.save()
            self.Cache.delete(pk)
            self.service.set(pk, data)
            return JsonResponse(status=202, data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        device = self.service.get(nr=pk, Cache=self.Cache)
        self.Cache.delete(pk)
        device.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
"""
@api_view(['POST'])
def add_items(request):
    device = DeviceSerializer(data=request.data)
    if device.is_valid():
        device.save()
        return JsonResponse(device.errors, status=202)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    devices = DeviceService.get_all
    if devices:
        data = DeviceSerializer(devices, many=True)
        return JsonResponse(status=202, data=data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
"""