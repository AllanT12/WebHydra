from rest_framework import serializers
from subscriptions.models import Subscriptions


class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'