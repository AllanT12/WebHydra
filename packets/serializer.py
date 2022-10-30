from rest_framework import serializers

import packets.models


class PacketsSerializer(serializers.ModelSerializer):
    model = packets.models.Packets
    fields = '__all__'