from django.urls import path
from .views import CheckoutsHistory

urlpatterns = [
    path('orders_history', CheckoutsHistory.as_view(), name='checkout_history'),
    path('orders_history<int:delivered>', CheckoutsHistory.as_view(), name='checkout_delivered_history')
]