# Generated by Django 5.0.3 on 2024-03-13 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_alter_rate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]
