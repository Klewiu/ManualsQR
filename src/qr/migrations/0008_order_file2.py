# Generated by Django 4.1.5 on 2023-01-23 22:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0007_alter_order_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['pdf'])], verbose_name='Plik'),
        ),
    ]
