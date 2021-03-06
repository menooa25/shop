import copy
import uuid

from django.core.mail import send_mail
from django.utils.translation import gettext as _
from rest_framework import status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer, CustomerProfileSerializer, AddressSerializer, RegisterSerializer, \
    CustomerProfileSerializerGet, CustomerProfileSerializerUpdate, ChangeCustomerPasswordSerializer, \
    CustomerEmailSerializer, ResetPasswordCodeSerializer
from ..models import CustomerModel, AddressModel

User = get_user_model()


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
                return Response({'msg': _('password doesnt match')})
            if CustomerModel.objects.filter(username=username):
                return Response({'msg': _('This emial is taken')}, status=status.HTTP_200_OK)
            CustomerModel.objects.create_user(username=username, password=password2, first_name=first_name,
                                              last_name=last_name, phone=phone)
            return Response({'msg': _('User created successfully')}, status=status.HTTP_201_CREATED)
        return Response({'msg': _('invalid data')}, status=status.HTTP_200_OK)

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
        return Response({'msg': _('Username or password is incorrect')}, status=status.HTTP_404_NOT_FOUND)


class ResetPassword(APIView):

    def post(self, request):
        try:
            serialized_email = CustomerEmailSerializer(data=request.data)
            if serialized_email.is_valid(raise_exception=True):
                email = serialized_email.data['email']
                customer = CustomerModel.objects.filter(username=email).first()
                if customer:
                    reset_password_code = str(uuid.uuid4())
                    customer.reset_password_code = reset_password_code
                    customer.save()
                    send_mail(
                        'Reset Password',
                        f'your reset password code is ( {reset_password_code} )',
                        'info@yoursite.com',
                        ['to@client.com'],
                        fail_silently=False,
                    )
            return Response({'msg': _('If emails exists reset password code will sent to it')}, status=status.HTTP_200_OK)
        except:
            return Response({'msg': _('Something went wrong')}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        reset_password_code_serialized = ResetPasswordCodeSerializer(data=request.data)
        if reset_password_code_serialized.is_valid(raise_exception=True):
            rest_password_code = reset_password_code_serialized.data['code']
            password1 = reset_password_code_serialized.data['password1']
            password2 = reset_password_code_serialized.data['password2']
            customer = CustomerModel.objects.filter(reset_password_code=rest_password_code).first()
            if customer:
                if password1 != password2:
                    return Response({'msg': _('password does not match')})
                customer_user = User.objects.get(id=customer.id)
                customer_user.set_password(password2)
                customer_user.reset_password_code = None
                customer_user.save()
                return Response({'msg': _('password updated successfully')})
        return Response({'msg': _('the code is not valid')}, status=status.HTTP_404_NOT_FOUND)


class CheckUserAuth(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(True)


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
            return Response({'msg': _('User updated successfully')}, status=status.HTTP_200_OK)
        return Response({'msg': _('Invalid data')}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        customer = CustomerModel.objects.get(id=request.user.id)
        serialized_customer = CustomerProfileSerializerGet(customer)
        response_data = dict(serialized_customer.data)
        address_id = response_data.get('address')
        # we want pass actual address not just address id
        if address_id:
            address = AddressModel.objects.get(id=address_id)
            response_data['address_str'] = str(address)
            response_data['address'] = AddressSerializer(address).data.values()
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
            return Response({'msg': _('address created and added to user')}, status=status.HTTP_201_CREATED)
        return Response({'msg': _('Invalid data')}, status=status.HTTP_400_BAD_REQUEST)


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
                return Response({'msg': _('password does not match')}, status=status.HTTP_406_NOT_ACCEPTABLE)
            user.set_password(passwords['password2'])
            user.save()
            return Response({'msg': _('password changed successfully')}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': _('invalid data')}, status=status.HTTP_400_BAD_REQUEST)
