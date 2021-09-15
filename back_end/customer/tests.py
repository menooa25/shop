import json

from django.test import TestCase
from django.urls import reverse
from .models import CustomerModel


class TestRegisterLogin(TestCase):
    def setUp(self) -> None:
        CustomerModel.objects.create_user(username='menooa2015@gmail.com',
                                          first_name='menooa',
                                          last_name='eskandarian',
                                          phone='09016718130',
                                          password='1332')

    def test_register_user(self):
        request_data = {'username': 'menooa2013@gmail.com',
                        'first_name': 'menooa',
                        'last_name': 'eskandarian',
                        'phone': '09016718130',
                        'password1': '1332',
                        'password2': '1332'}
        response = self.client.post(reverse('register_login'), data=request_data)

        assert response.data.get('msg') and response.data.get('msg') == "User created successfully"
        # existing username request
        request_data_2 = {'username': 'menooa2013@gmail.com',
                          'first_name': 'menooa',
                          'last_name': 'eskandarian',
                          'phone': '09016718130',
                          'password1': '1332',
                          'password2': '1332'}
        response_2 = self.client.post(reverse('register_login'), data=request_data_2)
        assert response_2.data.get('msg') and response_2.data.get('msg') == "This emial is taken"

    def test_login(self):
        request_data = {"username": "menooa2015@gmail.com", "password": "1332"}

        response = self.client.put(reverse('register_login'), data=request_data, content_type='application/json')
        assert response.data.get('token')

        request_data2 = {'username': 'menooa2019@gmail.com',
                         'password': '1332'}
        response2 = self.client.put(reverse('register_login'), data=request_data2, content_type='application/json')
        assert not response2.data.get('token')
