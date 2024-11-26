from django.db import models


class Hotel(models.Model):
    place = models.CharField(max_length=100)
