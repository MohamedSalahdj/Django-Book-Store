# Generated by Django 4.2.11 on 2024-03-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlist',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('disapproved', 'Disapproved')], max_length=15),
        ),
    ]
