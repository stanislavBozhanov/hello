from rest_framework import serializers
from .models import Event, Helloer, Friendship


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('band_id', 'timestamp')


class HelloerSerializer(serializers.ModelSerializer):

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

class FriendshipSerializer(serializers.ModelSerializer):

    user = HelloerSerializer(many=False, read_only=True)
    friend = HelloerSerializer(many=False, read_only=True)

    class Meta:
        model = Friendship
        fields = (
            'date',
            'user',
            'friend',
        )
