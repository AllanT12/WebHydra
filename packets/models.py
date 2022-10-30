from django.db import models

from devices.models import Devices


class Packets(models.Model):
    id = models.IntegerField(primary_key=True)
    packetinfo = models.TextField(blank=True, null=True)
    deviceid = models.ForeignKey(Devices, on_delete=models.CASCADE, blank=True, null=True)

# Create your models here.
