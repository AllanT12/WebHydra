from django.db import models

from devices.models import Devices


class Packets(models.Model):
    packetinfo = models.TextField(blank=True, null=True)
    deviceid = models.ForeignKey(Devices, on_delete=models.CASCADE, blank=True, null=True)

# Create your models here.
