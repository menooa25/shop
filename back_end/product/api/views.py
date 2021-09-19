from .serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from ..models import Product


class ProductViewSet(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
