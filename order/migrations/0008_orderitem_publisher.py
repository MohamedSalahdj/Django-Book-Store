# Generated by Django 5.0.3 on 2024-03-20 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_quantity'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='publisher',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.custompublisher'),
            preserve_default=False,
        ),
    ]