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

    def __str__(self):
        return f'{self.name} -- {self.price} -- {self.quantity}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    # product can have multiple images and main Image
    is_primary = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return f'{self.product} -- {self.is_primary}'

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'


class Discount(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='discount')
    percent = models.PositiveIntegerField()
    expire_date = models.DateTimeField()

    def __str__(self):
        return f'{self.product} -- {self.percent}'

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'
