from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AddressModel(models.Model):
    street = models.CharField(max_length=50)
    alley = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50, unique=True)
    number = models.CharField(max_length=6)
    dore_phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return f'{self.street} -- {self.postal_code}'


class CustomerModel(User):
    address = models.OneToOneField(AddressModel, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f'{self.first_name} -- {self.username}'

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
