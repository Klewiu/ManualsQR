# Generated by Django 4.1.5 on 2023-01-23 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0004_alter_order_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Plik'),
        ),
    ]
