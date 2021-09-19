from .views import ProductViewSet
from django.urls import path

urlpatterns = [
    path('', ProductViewSet.as_view(), name='products')
]
