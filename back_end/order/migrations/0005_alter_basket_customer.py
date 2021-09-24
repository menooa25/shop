# Generated by Django 3.2.7 on 2021-09-23 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_customermodel_phone'),
        ('order', '0004_alter_checkout_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customermodel'),
        ),
    ]