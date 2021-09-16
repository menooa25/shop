import copy
import hashlib
import json

from rest_framework import status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer, CustomerProfileSerializer, AddressSerializer, RegisterSerializer, \
    CustomerProfileSerializerGet, CustomerProfileSerializerUpdate, ChangeCustomerPasswordSerializer
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
        if not serialized_customer.is_valid():
            username = serialized_customer.data.get('username')
            password = serialized_customer.data.get('password')
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def if_data_exist_update(self, user, request_data):
        """ this will check witch customer data is passed and only that will update """
        user_obj = copy.copy(user)
        for key in request_data:
            setattr(user_obj, key, request_data[key])
        return user_obj

    def put(self, request):
        serialized_customer = CustomerProfileSerializerUpdate(data=request.data)
        if serialized_customer.is_valid(raise_exception=True):
            user = CustomerModel.objects.get(id=request.user.id)
            updated_user = self.if_data_exist_update(user=user, request_data=serialized_customer.data)
            updated_user.save()
            return Response({'msg': 'User updated successfully'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        customer = CustomerModel.objects.get(id=request.user.id)
        serialized_customer = CustomerProfileSerializerGet(customer)
        response_data = dict(serialized_customer.data)
        address_id = response_data.get('address')
        # we want pass actual address not just address id
        if address_id:
            address = AddressModel.objects.get(id=address_id)
            response_data['address'] = str(address)

        return Response(response_data)


class CustomerAddress(APIView):
    # taking token and checking valuable
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

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


class ChangeCustomerPassword(APIView):
    # taking token and checking valuable
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serialized_customer = ChangeCustomerPasswordSerializer(data=request.data)
        if serialized_customer.is_valid(raise_exception=True):
            passwords = serialized_customer.data
            if passwords['password1'] != passwords['password2'] or not check_password(passwords['password'],
                                                                                      user.password):
                return Response({'msg': 'password does not match'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.set_password(passwords['password2'])
            user.save()
            return Response({'msg': 'password changed successfully'}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': 'invalid data'}, status=status.HTTP_400_BAD_REQUEST)
