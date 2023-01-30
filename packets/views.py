from django.http import HttpResponse, JsonResponse
from injector import inject
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

import LogServices
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

    def get(self, request, pk):
        packets = self.service.get_all(self.Cache, pk)
        if packets:
            data = PacketsSerializer(packets, many=True)
            LogServices.write(packets.errors, 'ok')
            return JsonResponse(status=202, data=data.data, safe=False)
        else:
            LogServices.write(packets.errors, 'error at creating packet')
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        packet = PacketsSerializer(data=request.data)
        if packet.is_valid():
            packet.save()
            self.service.set(packet.data.get('id'), self.Cache)
            LogServices.write(packet.errors, 'ok')
            return JsonResponse(status=202, data=packet.data)
        else:
            LogServices.write(packet.errors, 'error at creating packet')
            return Response(packet.errors, status=400)

    def patch(self, request, pk):
        packet = self.service.get(nr=pk, Cache=self.Cache)
        data = PacketsSerializer(instance=packet, data=request.data)
        if data.is_valid():
            data.save()
            self.service.delete(pk, self.Cache)
            self.service.set(pk, self.Cache)
            LogServices.write(data.errors, 'ok')
            return JsonResponse(status=202, data=data.data)
        else:
            LogServices.write(data.errors, 'error at updating packet')
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        packet = self.service.get(nr=str(pk), Cache=self.Cache)
        self.Cache.delete(str(pk))
        packet.delete()
        LogServices.write(packet.errors, 'ok')
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
