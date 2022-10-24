# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Devices(models.Model):
    deivceid = models.IntegerField(db_column='DeivceId', primary_key=True)  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ownerid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='OwnerId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'devices'


class Packets(models.Model):
    id = models.IntegerField(primary_key=True)
    packetinfo = models.TextField(db_column='packetInfo', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.ForeignKey(Devices, models.DO_NOTHING, db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packets'
