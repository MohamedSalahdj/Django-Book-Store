# Generated by Django 5.0.3 on 2024-03-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_auto_20240312_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]