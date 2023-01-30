from django.http import JsonResponse
from django.shortcuts import render
from injector import inject
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import LogServices
from CacheService import CacheService
from subscriptions.serializer import SubSerializer
from subscriptions.services import SubService


class SubscriptionAPIView(APIView):

    @inject
    def setup(self, request, my_service: SubService, Cache: CacheService, **kwargs):
        self.service = my_service
        self.request = request
        self.kwargs = kwargs
        self.Cache = Cache

    def get(self, request):
        packets = self.service.get_all(self.Cache)
        if packets:
            data = SubSerializer(packets, many=False)
            LogServices.write(data.errors, 'ok')
            return JsonResponse(status=202, data=data.data)
        else:
            LogServices.write(packets.errors, 'error at creating user')
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        packet = SubSerializer(data=request.data)
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
        data = SubSerializer(instance=packet, data=request.data)
        if data.is_valid():
            data.save()
            self.service.delete(pk, self.Cache)
            self.service.set(pk, self.Cache)
            LogServices.write(data.errors, 'ok')
            return JsonResponse(status=202, data=data.data)
        else:
            LogServices.write(data.errors, 'error at creating user')
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        packet = self.service.get(nr=pk, Cache=self.Cache)
        self.service.delete(pk, self.Cache)
        packet.delete()
        LogServices.write('sub delete', 'ok')
        return Response(status=status.HTTP_202_ACCEPTED)


# Create your views here.
