from django.contrib import admin
from .models import Basket, Checkout, Shipping, Order

admin.site.register(Basket)
admin.site.register(Checkout)
admin.site.register(Shipping)
admin.site.register(Order)
