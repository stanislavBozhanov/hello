from django.db import models

# Create your models here.
class Event(models.Model):
    band_id = models.SmallIntegerField()
    timestamp = models.DateTimeField()


class HelloerProfile(models.Model):
    band_id = models.SmallIntegerField()
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.CharField(max_length=100)
