from django.conf.urls import url

from .views import event, login, profile


urlpatterns = [
    url(r'^api/event', event, name='event'),
    url(r'^api/login', login, name='login'),
    url(r'^api/profile', profile, name='profile'),
]
