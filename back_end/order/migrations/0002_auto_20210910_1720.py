# Generated by Django 3.2.7 on 2021-09-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('customer_phone', models.CharField(max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('products', models.JSONField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'سبد خرید', 'verbose_name_plural': 'سبد های خرید'},
        ),
        migrations.AlterModelOptions(
            name='checkout',
            options={'verbose_name': 'تسویه حساب', 'verbose_name_plural': 'تسویه حساب ها'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارشات'},
        ),
        migrations.AlterModelOptions(
            name='shipping',
            options={'verbose_name': 'ارسال', 'verbose_name_plural': 'ارسال ها'},
        ),
        migrations.AlterField(
            model_name='shipping',
            name='status',
            field=models.CharField(choices=[('IN_PROCESS', 'IN_PROCESS'), ('FACTORED', 'FACTORED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('CANCELED', 'CANCELED')], default='IN_PROCESS', max_length=20),
        ),
    ]
