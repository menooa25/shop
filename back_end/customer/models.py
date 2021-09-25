from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AddressModel(models.Model):
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    number = models.CharField(max_length=6)
    dore_phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return f'خیابان {self.street} / کوچه {self.alley} / کد پستی{self.postal_code} / پلاک{self.number} / زنگ {self.dore_phone}'


class CustomerModel(User):
    address = models.OneToOneField(AddressModel, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20)
    reset_password_code = models.CharField(max_length=50, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.first_name} -- {self.username}'

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'


class DiscountModel(models.Model):
    code = models.CharField(max_length=20)
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE, related_name='discount')
    percent = models.PositiveIntegerField()
    expire_date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} -- {self.percent}'

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'
