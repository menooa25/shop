from django.db import models

from customer.models import CustomerModel
from product.models import Product


class Basket(models.Model):
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.customer.username


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
