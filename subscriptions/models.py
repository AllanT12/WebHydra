from django.db import models


class Subscriptions(models.Model):
    tier = models.TextField()
    days = models.IntegerField(null=False, blank=False)
