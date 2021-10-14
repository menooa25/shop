from django.contrib import admin
from .models import CustomerModel, AddressModel, DiscountModel


@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('username', 'phone', 'address', 'first_name', 'last_name')


admin.site.register(AddressModel)
admin.site.register(DiscountModel)
