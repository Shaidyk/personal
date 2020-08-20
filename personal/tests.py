from rest_framework.test import APITestCase
from .models import *


class SerializerTestCase(APITestCase):
    def test_create_courier(self):
        data = {
            'first_name': 'Courier',
            'last_name': 'TheBest',
            'region': '1',
        }

        response = self.client.post(
            '/courier/',
            data=data)

        self.assertEqual(response.status_code, 201)

        Client.objects.get(**data)
