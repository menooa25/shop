# Generated by Django 3.2.7 on 2021-09-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customermodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressmodel',
            name='postal_code',
            field=models.CharField(max_length=50),
        ),
    ]