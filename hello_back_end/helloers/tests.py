from datetime import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from .models import Event, Helloer, Friendship


class HelloerTests(TestCase):

    def setUp(self):
        self.viki_helloer = Helloer.objects.create(
            band_id=32,
            name='Viki',
            age=21,
            telephone='+359888888888',
            email='vikiviki@viki.viki',
            facebook='vikiviki'
        )
        self.stenly_helloer = Helloer.objects.create(
            band_id=23,
            name='Stenly',
            age=24,
            telephone='+359888888889',
            email='stenly@stenly.stenly',
            facebook='stenlystenly'
        )


class EventTests(TestCase):

    def setUp(self):
        self.viki_helloer = Helloer.objects.create(
            band_id=32,
            name='Viki',
            age=21,
            telephone='+359888888888',
            email='vikiviki@viki.viki',
            facebook='vikiviki'
        )
        self.stenly_helloer = Helloer.objects.create(
            band_id=23,
            name='Stenly',
            age=24,
            telephone='+359888888889',
            email='stenly@stenly.stenly',
            facebook='stenlystenly'
        )

    def test_event_creation(self):
        data = {
            'band_id': 23,
            'timestamp': datetime.now(),
        }
        url = reverse('helloers:event')
        self.client.post(url, data, format='json')
        self.assertEqual(Event.objects.all().count(), 1)

    def test_get_profile_data(self):
        data = {
            'user': 'Viki'
        }
        url = reverse('helloers:profile')
        response = self.client.get(url, data, format='json')
        self.assertEqual(Event.objects.all().count(), 1)
        print(response.data)
