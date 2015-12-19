from django.contrib import admin

# Register your models here.
from .models import Event, Helloer, Friendship


class EventAdmin(admin.ModelAdmin):
    list_display = ('band_id', 'timestamp')

    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)


class HelloerAdmin(admin.ModelAdmin):
    list_display = (
        'band_id',
        'name',
        'age',
        'telephone',
        'email',
        'facebook'
    )

    class Meta:
        model = Helloer

admin.site.register(Helloer, HelloerAdmin)

class FriendshipAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'friend_id'
    )

    class Meta:
        model = Friendship

admin.site.register(Friendship, FriendshipAdmin)
