# Generated by Django 4.1.5 on 2023-02-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0015_order_file2language_order_filelanguage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstLabel', models.CharField(max_length=15, verbose_name='Tytuł pierwszego slajdu')),
                ('firstCaption', models.CharField(max_length=15, verbose_name='Tekst pierwszego slajdu')),
                ('secondLabel', models.CharField(max_length=15, verbose_name='Tytuł drugiego slajdu')),
                ('secondCaption', models.CharField(max_length=15, verbose_name='Tekst drugiego slajdu')),
                ('thirdLabel', models.CharField(max_length=15, verbose_name='Tytuł trzeciego slajdu')),
                ('thirdCaption', models.CharField(max_length=15, verbose_name='Tekst trzeciego slajdu')),
                ('firstSlide', models.FileField(blank=True, null=True, upload_to='marketing', verbose_name='Pierwszy slajd')),
                ('secondSlide', models.FileField(blank=True, null=True, upload_to='marketing', verbose_name='Drugi slajd')),
                ('thirdSlide', models.FileField(blank=True, null=True, upload_to='marketing', verbose_name='Trzeci slajd')),
            ],
            options={
                'verbose_name': 'Baner Markegin',
                'verbose_name_plural': 'Banery Marketingowe',
            },
        ),
    ]