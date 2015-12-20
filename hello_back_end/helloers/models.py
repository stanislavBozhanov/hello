from django.db import models

# Create your models here.
class Event(models.Model):
    band_id = models.SmallIntegerField()
    timestamp = models.DateTimeField()


class Helloer(models.Model):
    band_id = models.SmallIntegerField()
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Friendship(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Helloer, related_name='friendship_requests_sent')
    friend = models.ForeignKey(Helloer, related_name='friendship_requests_received')
