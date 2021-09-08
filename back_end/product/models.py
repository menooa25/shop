from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()


class Discount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    percent = models.PositiveIntegerField()
