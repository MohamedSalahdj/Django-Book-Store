# Generated by Django 4.2.11 on 2024-03-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_publisher_email_alter_publisher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='certificate',
            field=models.FileField(null=True, upload_to='certificate/'),
        ),
    ]
