from rest_framework.test import APITestCase

from .serializers import *


class CourierSerializerTestCase(APITestCase):

    def test_create_courier(self):
        data = {
            'first_name': 'Ivan',
            'last_name': 'Petrov',
            'region': 'Odessa',
        }
        response = self.client.post('/couriers/', data=data)
        print(response.data)
        self.assertEqual(response.status_code, 201)
        CourierSerializer.objects.get(**data)
