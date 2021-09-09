from django.contrib import admin
from .models import CustomerModel, AddressModel, DiscountModel

admin.site.register(CustomerModel)
admin.site.register(AddressModel)
admin.site.register(DiscountModel)
