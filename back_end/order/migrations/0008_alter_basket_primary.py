# Generated by Django 3.2.7 on 2021-09-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20210923_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='primary',
            field=models.BooleanField(default=True),
        ),
    ]
