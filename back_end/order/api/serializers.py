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

    def validate(self, attrs):
        super().validate(attrs)
        product_quantity = attrs['product'].quantity
        quantity = attrs['quantity']
        if product_quantity < quantity:
            raise serializers.ValidationError('there is not enough product to parches ')
        return attrs

    def save(self, **kwargs):
        super().save(**kwargs)
        product_id = self.data.get('product')
        product = Product.objects.get(id=product_id)
        product.quantity -= self.data.get('quantity')
        product.save()

    class Meta:
        model = Order
        fields = '__all__'


class AddToCheckout(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = '__all__'
