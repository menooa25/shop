# Generated by Django 3.2.7 on 2021-09-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_checkout_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
