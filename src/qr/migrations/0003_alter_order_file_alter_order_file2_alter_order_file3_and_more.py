# Generated by Django 4.1.5 on 2023-02-12 20:13

from django.db import migrations, models
import qr.validators


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_alter_order_file_alter_order_file2_alter_order_file3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[qr.validators.validate_file_size, qr.validators.validate_pdf], verbose_name='Instrukcja I'),
        ),
        migrations.AlterField(
            model_name='order',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[qr.validators.validate_file_size, qr.validators.validate_pdf], verbose_name='Instrukcja II'),
        ),
        migrations.AlterField(
            model_name='order',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[qr.validators.validate_file_size, qr.validators.validate_pdf], verbose_name='Instrukcja III'),
        ),
        migrations.AlterField(
            model_name='order',
            name='file4',
            field=models.FileField(blank=True, null=True, upload_to='media/', validators=[qr.validators.validate_file_size, qr.validators.validate_pdf], verbose_name='Instrukcja IV'),
        ),
    ]
