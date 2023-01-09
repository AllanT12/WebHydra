from rest_framework import serializers

import devices.models


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = devices.models.Devices
        fields = '__all__'