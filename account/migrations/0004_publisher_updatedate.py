# Generated by Django 5.0.3 on 2024-03-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_publisher_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='updatedate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]