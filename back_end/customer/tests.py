import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

from .models import CustomerModel


def create_user():
    customer = CustomerModel.objects.create_user(username='menooa2015@gmail.com',
                                                 first_name='menooa',
                                                 last_name='eskandarian',
                                                 phone='09016718130',
                                                 password='1332',
                                                 reset_password_code='some_codesome_codesome_codesome_codesome')
    return customer


class TestRegisterLogin(TestCase):
    def setUp(self) -> None:
        create_user()

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


class TestResetPassword(TestCase):
    def setUp(self) -> None:
        create_user()

    def test_reset_password(self):
        reset_password_code = 'some_codesome_codesome_codesome_codesome'
        request_data = {'code': reset_password_code,
                        'password1': '1332',
                        'password2': '1332'}
        response = self.client.put(reverse('reset_password'), data=request_data, content_type='application/json')
        assert response.data.get('msg') == 'password updated successfully'

    def test_reset_password_request(self):
        request_data = {"email": 'menooa2015@gmail.com'}
        response = self.client.post(reverse('reset_password'), data=request_data)
        assert response.status_code == 200


class TestCheckUserAuth(TestCase):
    def setUp(self) -> None:
        customer = create_user()
        token = Token(user=customer)
        token.save()
        self.token = str(token)

    def test_user_auth(self):
        response = self.client.get(reverse('check_user_auth'), AUTHORIZATION='Token ' + self.token)
        assert response.data
