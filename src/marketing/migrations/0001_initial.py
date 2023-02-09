# Generated by Django 4.1.5 on 2023-02-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40, verbose_name='Tytuł slajdu')),
                ('slide', models.FileField(blank=True, null=True, upload_to='marketing', verbose_name='Grafika slajdu')),
            ],
            options={
                'verbose_name': 'Baner Marketingowy',
                'verbose_name_plural': 'Banery Marketingowe',
            },
        ),
    ]