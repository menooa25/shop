from django.urls import path
from .views import RegisterLogin, CustomerProfile, CustomerAddress,ChangeCustomerPassword

urlpatterns = [
    path('register_login', RegisterLogin.as_view(), name='register_login'),
    # getting user data and updating
    path('customer_profile', CustomerProfile.as_view(), name='customer_profile'),
    path('customer_address', CustomerAddress.as_view(), name='customer_address'),
    path('customer_change_password', ChangeCustomerPassword.as_view(), name='customer_change_password'),
]
