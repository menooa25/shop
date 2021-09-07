from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from .serializers import CustomerSerializer
from ..models import CustomerModel


class RegisterLogin(APIView):
    def post(self, request):
        # registering user
        # we are using phone number as username
        serialized_customer = CustomerSerializer(data=request.data)
        if serialized_customer.is_valid():
            username = serialized_customer.data.get('username')
            password = serialized_customer.data.get('password')
            CustomerModel.objects.create_user(username=username, password=password)
            return Response({'msg': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'msg': 'This username is taken'}, status=status.HTTP_200_OK)

    def get(self, request):
        serialized_customer = CustomerSerializer(data=request.data)
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


class UpdateCustomer(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
