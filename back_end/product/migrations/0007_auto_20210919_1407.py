# Generated by Django 3.2.7 on 2021-09-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20210919_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]