from django.conf.urls import url

from .views import event, login, profile, friends


urlpatterns = [
    url(r'^api/event', event, name='event'),
    url(r'^api/login', login, name='login'),
    url(r'^api/profile', profile, name='profile'),
    url(r'^api/friends', friends, name='friends')
]
