from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from reservation.models import Menu
from reservation.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title='Test Item 1', price=10.99, inventory=5)
        Menu.objects.create(title='Test Item 2', price=8.99, inventory=3)
        Menu.objects.create(title='Test Item 3', price=12.99, inventory=7)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)