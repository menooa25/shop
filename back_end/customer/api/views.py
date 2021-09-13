import hashlib

from rest_framework import status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer, CustomerProfileSerializer, AddressSerializer, RegisterSerializer
from ..models import CustomerModel, AddressModel


class RegisterLogin(APIView):
    def post(self, request):
        # registering user
        # we are using username as email
        serialized_customer = RegisterSerializer(data=request.data)
        if serialized_customer.is_valid(raise_exception=True):
            username = serialized_customer.data.get('username')
            first_name = serialized_customer.data.get('first_name')
            last_name = serialized_customer.data.get('last_name')
            phone = serialized_customer.data.get('phone')
            password1 = serialized_customer.data.get('password1')
            password2 = serialized_customer.data.get('password2')
            if password1 != password2:
                return Response({'msg': 'password doesnt match'})
            if CustomerModel.objects.filter(username=username):
                return Response({'msg': 'This emial is taken'}, status=status.HTTP_200_OK)
            CustomerModel.objects.create_user(username=username, password=password2, first_name=first_name,
                                              last_name=last_name, phone=phone)
            return Response({'msg': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'invalid data'}, status=status.HTTP_200_OK)

    def put(self, request):
        serialized_customer = LoginSerializer(data=request.data)
        # when is_valid() return true that shows that username exists
        if serialized_customer.is_valid():
            username = serialized_customer.data.get('username')
            password = serialized_customer.data.get('password')
            print(make_password(password))
            if authenticate(username=username, password=password):
                # if user authenticated we will return auth token
                user = CustomerModel.objects.get(username=username)
                # if token is already created it will be refresh
                old_token = Token.objects.filter(user=user)
                if old_token:
                    old_token.delete()
                token = Token.objects.create(user=user)
                return Response({'token': str(token)}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': 'Username or password is incorrect'}, status=status.HTTP_404_NOT_FOUND)


class CustomerProfile(APIView):
    # taking token and checking valuable
    authentication_classes = [authentication.TokenAuthentication]

    # updating profile firstname lastname and phone
    def put(self, request):
        serialized_customer = CustomerProfileSerializer(data=request.data)
        if serialized_customer.is_valid(raise_exception=True):
            user = request.user
            user.first_name = serialized_customer.data.get('first_name')
            user.last_name = serialized_customer.data.get('last_name')
            user.username = serialized_customer.data.get('username')
            user.set_password(serialized_customer.data.get('password'))
            user.save()
            return Response({'msg': 'User updated successfully'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class CustomerAddress(APIView):
    # taking token and checking valuable
    authentication_classes = [authentication.TokenAuthentication]

    def put(self, request):
        # creating address and updating if exists
        serialized_address = AddressSerializer(data=request.data)
        if serialized_address.is_valid():
            user = request.user
            customer = CustomerModel.objects.get(id=user.id)
            # if user has address it will delete and replace with new one
            if customer.address:
                address_id = customer.address.id
                address = AddressModel.objects.get(id=address_id)
                address.delete()
            address = serialized_address.save()
            customer.address = address
            customer.save()
            return Response({'msg': 'address created and added to user'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
