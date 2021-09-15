from ..models import CustomerModel, AddressModel
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    # remember this username used as email
    username = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone = serializers.RegexField('^[0-9]*[0-9]$')
    password1 = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)


class LoginSerializer(serializers.ModelSerializer):
    # remember this username used as email
    # username = serializers.EmailField()

    class Meta:
        model = CustomerModel
        fields = ['username', 'password']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'


class CustomerProfileSerializer(serializers.ModelSerializer):
    # remember this username used as email
    username = serializers.EmailField()

    class Meta:
        model = CustomerModel
        fields = ['first_name', 'last_name', 'username', 'password']


class CustomerProfileSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['first_name', 'last_name', 'username', 'address', 'phone']


class CustomerProfileSerializerUpdate(serializers.ModelSerializer):
    username = serializers.EmailField(required=False)
    phone = serializers.RegexField('^[0-9]*[0-9]$', required=False)

    class Meta:
        model = CustomerModel
        fields = ['first_name', 'last_name', 'username', 'phone']


class ChangeCustomerPasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)

    class Meta:
        model = CustomerModel
        fields = ['password', 'password1', 'password2']
