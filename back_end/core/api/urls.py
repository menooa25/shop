from django.urls import path, include

urlpatterns = [
    path('customers/', include('customer.api.urls'))
]
