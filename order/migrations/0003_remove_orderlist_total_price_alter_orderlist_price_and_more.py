# Generated by Django 4.2.11 on 2024-03-14 23:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderlist_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlist',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='product_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
