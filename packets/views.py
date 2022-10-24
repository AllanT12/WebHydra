from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from .Serializer import PacketsSerializer
from .models import Packets

@api_view(['POST'])
def add_items(request):
    packet = PacketsSerializer(data=request.data)

    # validating for already existing data
    if Packets.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if packet.is_valid():
        packet.save()
        return Response(packet.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        packets = Packets.objects.filter(**request.query_param.dict())
    else:
        packets = Packets.objects.all()

    # if there is something in items else raise error
    if packets:
        data = PacketsSerializer(packets, many=True)
        return Response(data=data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    item = Packets.objects.get(pk=pk)
    data = PacketsSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    packet = get_object_or_404(Packets, pk=pk)
    packet.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
# Create your views here.
