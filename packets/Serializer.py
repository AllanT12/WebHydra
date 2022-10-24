from django.db.models import fields
from rest_framework import serializers
from .models import Packets

class PacketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packets
        fields = ['id', 'packetinfo', 'deviceid']
