from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی ها'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField()
    short_description = models.TextField(max_length=250)
    long_description = models.TextField()

    def __str__(self):
        return f'{self.name} -- {self.price} -- {self.quantity}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'