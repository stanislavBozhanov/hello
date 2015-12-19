from rest_framework import serializers
from .models import Event, HelloerProfile


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('band_id', 'timestamp')


class HellowerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = HelloerProfile
        fields = (
            'band_id',
            'name',
            'age',
            'telephone',
            'email',
            'facebook'
        )
