from ..models import CustomerModel, AddressModel
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    # remember this username used as phone number
    username = serializers.RegexField(regex='^([0-9]*[0-9])$')

    class Meta:
        model = CustomerModel
        fields = ['username', 'password']


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressModel
        fields = '__all__'


class CustomerProfileSerializer(serializers.ModelSerializer):
    # remember this username used as phone number
    username = serializers.RegexField(regex='^([0-9]*[0-9])$')

    class Meta:
        model = CustomerModel
        fields = ['first_name', 'last_name', 'username']
