from django.conf.urls import url

from .views import event


urlpatterns = [
    url(r'^api/event', event, name='event'),
]
