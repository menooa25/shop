from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from ..models import Shipping, Order


class CheckoutsHistory(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # querying orders to find product_name: quantity, status and calculate total price
    def pretty_print_history(self, orders, status):
        products = list()
        total_price = 0
        for order in orders:
            products.append({
                "name": order.product.name,
                "quantity": order.quantity
            })
            total_price += order.product.price * order.quantity

        pretty_history = {
            "product": products,
            "total_price": float(total_price),
            "status": status
        }
        return pretty_history

    def get(self, request, delivered=0):
        customer_id = request.user.id
        if delivered:
            shipping = Shipping.objects.filter(checkout__basket__customer_id=customer_id, status=Shipping.DELIVERED)
        else:
            shipping = Shipping.objects.filter(checkout__basket__customer_id=customer_id)
        if shipping:
            checkouts = []
            # there is a multiple shipping in multiple time with multiple orders
            for shipping in shipping:
                basket = shipping.checkout.basket
                orders = Order.objects.filter(basket_id=basket.id)
                checkouts.append(self.pretty_print_history(orders, shipping.status))
            return Response(checkouts)
        return Response('')
