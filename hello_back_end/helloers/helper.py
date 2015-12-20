from .models import Event, Helloer, Friendship
import datetime


def friendship_request():
    if Event.objects.all().count() > 1:
        events = Event.objects.all().order_by('-id')[:2]
        user = Helloer.objects.get(band_id=events[0].band_id)
        friend = Helloer.objects.get(band_id=events[1].band_id)
        if (events[0].timestamp - events[1].timestamp < datetime.timedelta(60)) and user != friend:
            if not Friendship.objects.filter(user=user, friend=friend).exists():
                Friendship.objects.create(user=user, friend=friend)
                Friendship.objects.create(user=friend, friend=user)
