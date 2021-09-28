from django.urls import path
from .views import CheckoutsHistory, BasketView, VerifyDiscount, OrderProduct

urlpatterns = [
    path('orders_history', CheckoutsHistory.as_view(), name='checkout_history'),
    path('orders_history<int:delivered>', CheckoutsHistory.as_view(), name='checkout_delivered_history'),
    path('basket', BasketView.as_view(), name='basket'),
    path('discount', VerifyDiscount.as_view(), name='verify_discount'),
    path('buy', OrderProduct.as_view(), name='buy_product')
]
