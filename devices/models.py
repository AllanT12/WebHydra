from django.db import models

from users.models import NewUser


class Devices(models.Model):
    deivceid = models.IntegerField(primary_key=True)
    devicename = models.CharField(max_length=10, blank=True, null=True)
    ownerid = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)

# Create your models here.
