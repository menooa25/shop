# Generated by Django 3.2.7 on 2021-09-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_checkout_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=100, null=True),
        ),
    ]
