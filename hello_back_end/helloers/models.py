from django.db import models

# Create your models here.
class Event(models.Model):
    band_id = models.SmallIntegerField()
    timestamp = models.DateTimeField()

