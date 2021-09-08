from django.contrib import admin
from .models import Product, Category, Discount, Image

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Image)
