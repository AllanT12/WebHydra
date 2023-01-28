from django.http import HttpResponse, JsonResponse
from injector import inject
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .serializer import PacketsSerializer
from .models import Packets
from .services import PacketService
from CacheService import CacheService


class PacketAPIView(APIView):

    @inject
    def setup(self, request, my_service: PacketService, Cache: CacheService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs
        self.Cache = Cache

    def get(self, request):
        packets = self.service.get_all(self.Cache)
        if packets:
            data = PacketsSerializer(packets, many=False)
            return JsonResponse(status=202, data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        packet = PacketsSerializer(data=request.data)
        if packet.is_valid():
            packet.save()
            self.Cache.set(packet.get_value('id'), packet)
            return JsonResponse(status=202, data=packet.data)
        else:
            return Response(packet.errors, status=400)

    def patch(self, request, pk):
        packet = self.service.get(nr=pk, Cache=self.Cache)
        data = PacketsSerializer(instance=packet, data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(status=202, data=data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        packet = self.service.get(nr=pk, Cache=self.Cache)
        self.Cache.delete(pk)
        packet.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
"""
@api_view(['POST'])
def add_items(request):
    packet = PacketsSerializer(data=request.data)

    if packet.is_valid():
        packet.save()
        return JsonResponse(packet.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request, service: PacketService):
    packets = service.get_all
    if packets:
        data = PacketsSerializer(packets, many=True)
        return JsonResponse(status=202, data=data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk, service: PacketService):
    packet = service.get(nr=pk)
    data = PacketsSerializer(instance=packet, data=request.data)

    if data.is_valid():
        data.save()
        return JsonResponse(status=202, data=data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk, service: PacketService):
    packet = service.get(nr=pk)
    packet.delete()
    return Response(status=status.HTTP_202_ACCEPTED)"""
