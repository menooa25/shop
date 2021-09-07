from django.urls import path
from .views import RegisterLogin, UpdateCustomer

urlpatterns = [
    path('register_login', RegisterLogin.as_view(), name='register_login'),
    # getting user data and updating
    path('update', UpdateCustomer.as_view(), name='update_customer')
]
