import copy

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.views import APIView
from ..models import Product, Category


class Products(APIView):

    def get(self, request, _id=None):
        products = None
        page_size = 3
        if _id:
            products = ProductSerializer(get_object_or_404(Product, pk=_id)).data
        else:
            # getting all serialized products
            products = ProductSerializer(Product.objects.all(), many=True).data
            paginated_products = []
            products_in_page = []
            for product in products:
                if len(products_in_page) < page_size:
                    products_in_page.append(product)
                if len(products_in_page) == page_size:
                    paginated_products.append(copy.copy(products_in_page))
                    products_in_page.clear()
            paginated_products.append(copy.copy(products_in_page))
            products = paginated_products
        return Response(products)


class SearchProducts(APIView):
    def get(self, request, search):
        products = ProductSerializer(Product.objects.filter(name__icontains=search.lower()), many=True)
        return Response(products.data)


class CategoryProduct(APIView):
    def get(self, request, _id):
        products = ProductSerializer(Product.objects.filter(category_id=_id), many=True).data
        page_size = 3
        paginated_products = []
        products_in_page = []
        for product in products:
            if len(products_in_page) < page_size:
                products_in_page.append(product)
            if len(products_in_page) == page_size:
                paginated_products.append(copy.copy(products_in_page))
                products_in_page.clear()
        paginated_products.append(copy.copy(products_in_page))
        products = paginated_products
        return Response(products)


class Categories(APIView):
    def get(self, request):
        category = CategorySerializer(Category.objects.all(), many=True)
        return Response(category.data)
