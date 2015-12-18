from rest_framework import serializers
from helloers.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('band_id', 'timestamp')