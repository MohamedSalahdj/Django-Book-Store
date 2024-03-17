# Generated by Django 4.2.11 on 2024-03-14 23:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_orderlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='status',
            field=models.CharField(max_length=15),
        ),
    ]