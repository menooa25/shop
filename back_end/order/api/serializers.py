from rest_framework import serializers

from product.models import Product
from ..models import Order


#
# class SingleBasketProductSerializer(serializers):
#     name = serializers.CharField(max_length=100)
#     price = serializers.FloatField()
#
#
# class BasketProductsSerializer(serializers):
#     order = serializers.ListSerializer()

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','quantity']


class OrderSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer()

    class Meta:
        model = Order
        fields = ['quantity', 'product']
