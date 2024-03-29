# Generated by Django 4.2.11 on 2024-03-22 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_quantity_order_total_orderitem_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
    ]
