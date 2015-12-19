from django.contrib import admin

# Register your models here.
from helloers.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('band_id', 'timestamp')

    class Meta:
        model = Event

admin.site.register(Event, EventAdmin)
