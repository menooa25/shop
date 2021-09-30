from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from customer.models import DiscountModel, CustomerModel
from ..models import Shipping, Order, Basket, Checkout
from .serializers import OrderSerializer, OrderSimpleSerializer


class CheckoutsHistory(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # querying orders to find product_name: quantity, status and calculate total price
    def pretty_print_history(self, orders, status,checkout):
        products = list()
        total_price = checkout.total_price
        for order in orders:
            products.append({
                "name": order.product.name,
                "quantity": order.quantity
            })

        pretty_history = {
            "product": products,
            "total_price": float(total_price),
            "status": status
        }
        return pretty_history

    def get(self, request, delivered=0):
        customer_id = request.user.id
        if delivered:
            shipping = Shipping.objects.filter(checkout__basket__customer_id=customer_id).exclude(
                status=Shipping.DELIVERED)
        else:
            shipping = Shipping.objects.filter(checkout__basket__customer_id=customer_id)
        if shipping:
            checkouts = []
            # there is a multiple shipping in multiple time with multiple orders
            for shipping in shipping:
                basket = shipping.checkout.basket
                orders = Order.objects.filter(basket_id=basket.id)
                checkouts.append(self.pretty_print_history(orders, shipping.status,shipping.checkout))
            return Response(checkouts)
        return Response('')


class BasketView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        customer_id = request.user.id
        orders = Order.objects.filter(basket__primary=True, basket__customer_id=customer_id)
        serialized_order = OrderSerializer(orders, many=True)

        return Response(serialized_order.data)


class VerifyDiscount(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        customer_id = request.user.id
        discount_code = request.data.get('code')
        discount = DiscountModel.objects.filter(customer_id=customer_id, code=discount_code).first()
        if discount:
            return Response(discount.percent)
        return Response(0)


class OrderProduct(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        customer_id = request.user.id
        request_data = {}
        request_data['product'] = int(request.data.get('product'))
        request_data['quantity'] = int(request.data.get('quantity'))
        basket = Basket.objects.filter(customer_id=customer_id, primary=True).first()
        if not basket:
            basket = Basket(customer=CustomerModel.objects.get(id=customer_id))
            basket.save()
            request_data['basket'] = basket.id
        else:
            request_data['basket'] = basket.id
        serialized_product_order = OrderSimpleSerializer(data=request_data)
        if serialized_product_order.is_valid(raise_exception=True):
            serialized_product_order.save()
            return Response({'msg': 'product added to basket'})
        return Response({"msg": 'something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddToCheckout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_total_price(self, basket):
        total_price = 0
        for order in basket.order_set.all():
            quantity = order.quantity
            price = order.product.price
            total_price += quantity * price
        return total_price

    def post(self, request):
        customer_id = request.user.id
        basket = Basket.objects.filter(customer_id=customer_id, primary=True).first()
        if not basket.primary:
            return Response({'msg': 'you dont have primary basket'})
        discount_code = request.data.get('code')
        discount = DiscountModel.objects.filter(customer_id=customer_id, code=discount_code).first()
        total_price = float(self.get_total_price(basket))
        if discount:
            discount_percent = discount.percent / 100
            total_price = total_price - (total_price * discount_percent)
        basket.primary = False
        basket.save()
        checkout = Checkout(basket=basket, is_paid=True,total_price=total_price)
        checkout.save()
        shipping = Shipping(status=Shipping.IN_PROCESS, checkout=checkout)
        shipping.save()
        return Response({'msg': 'thanks for purchase'})
