from django.urls import path
from .views import RegisterLogin, CustomerProfile, CustomerAddress, ChangeCustomerPassword, ResetPassword,CheckUserAuth

urlpatterns = [
    path('register_login', RegisterLogin.as_view(), name='register_login'),
    path('reset_password', ResetPassword.as_view(), name='reset_password'),
    # getting user data and updating
    path('customer_profile', CustomerProfile.as_view(), name='customer_profile'),
    path('customer_address', CustomerAddress.as_view(), name='customer_address'),
    path('customer_change_password', ChangeCustomerPassword.as_view(), name='customer_change_password'),
    path('check_user_auth', CheckUserAuth.as_view(), name='check_user_auth'),
]
