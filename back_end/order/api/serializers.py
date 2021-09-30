from rest_framework import serializers

from product.models import Product
from ..models import Order, Checkout


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer()

    class Meta:
        model = Order
        fields = ['quantity', 'product']


class OrderSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class AddToCheckout(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'
