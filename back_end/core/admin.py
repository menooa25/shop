from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    # pass
    # fields = ['username', 'password', 'groups', 'date_joined', 'is_staff']
    fields = ['username', 'password']
