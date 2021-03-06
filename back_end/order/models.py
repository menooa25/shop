from django.db import models

from customer.models import CustomerModel
from product.models import Product


class Basket(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    # if primary is true that means this basket is customer in time working basket
    primary = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return f"{self.customer.username} {self.customer_id} -- {self.id}"


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return f'{self.product} -- {self.quantity}'


class Checkout(models.Model):
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
    total_price = models.FloatField(default=-1, blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'تسویه حساب'
        verbose_name_plural = 'تسویه حساب ها'

    def __str__(self):
        return f'{self.basket} -- {self.is_paid}'


class Shipping(models.Model):
    # remember to log checkout details every time!
    checkout = models.OneToOneField(Checkout, null=True, on_delete=models.SET_NULL)
    # choice values are same string for readability in database
    IN_PROCESS = 'IN_PROCESS'
    FACTORED = 'FACTORED'
    DELIVERING = 'DELIVERING'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'
    choices = [(IN_PROCESS, IN_PROCESS),
               (FACTORED, FACTORED),
               (DELIVERING, DELIVERING),
               (DELIVERED, DELIVERED),
               (CANCELED, CANCELED)]
    status = models.CharField(choices=choices, max_length=20, default=IN_PROCESS)

    class Meta:
        verbose_name = 'ارسال'
        verbose_name_plural = 'ارسال ها'

    def __str__(self):
        return f'{self.checkout} -- {self.status}'


class OrdersHistory(models.Model):
    # use this if you are not using logfile history
    order_time = models.DateTimeField(auto_now_add=True)
    customer_phone = models.CharField(max_length=20)
    total_price = models.DecimalField(decimal_places=2, max_digits=12)
    products = models.JSONField()

    class Meta:
        verbose_name = 'تاریخچه سفارش'
        verbose_name_plural = 'تاریخچه سفارشات'

    def __str__(self):
        return f'{self.customer_phone} -- {self.total_price} -- {self.order_time}'
