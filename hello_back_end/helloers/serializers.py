from rest_framework import serializers
from .models import Event, Helloer, Friendship


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('band_id', 'timestamp')


class HellowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Helloer
        fields = (
            'band_id',
            'name',
            'age',
            'telephone',
            'email',
            'facebook'
        )

class HellowerFriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Helloer
        fields = (
            'date'
            'band_id',
            'name',
            'age',
            'telephone',
            'email',
            'facebook'
        )
