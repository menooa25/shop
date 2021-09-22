from .views import Products, SearchProducts, CategoryProduct, Categories
from django.urls import path

urlpatterns = [
    path('', Products.as_view(), name='products'),
    # searching in products name
    path('search/<str:search>', SearchProducts.as_view(), name='search_product'),
    path('<int:_id>', Products.as_view(), name='product_by_id'),
    # getting products by category id
    path('category/<int:_id>', CategoryProduct.as_view(), name='search_by_category'),
    # getting categories list
    path('categories', Categories.as_view(), name='category_list'),

]
