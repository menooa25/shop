# Generated by Django 3.2.7 on 2021-09-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210910_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordershistory',
            options={'verbose_name': 'تاریخچه سفارش', 'verbose_name_plural': 'تاریخچه سفارشات'},
        ),
        migrations.AlterField(
            model_name='checkout',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.basket'),
        ),
    ]