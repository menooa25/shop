from django.contrib import admin
from .models import CustomerModel, AddressModel

admin.site.register(CustomerModel)
admin.site.register(AddressModel)
