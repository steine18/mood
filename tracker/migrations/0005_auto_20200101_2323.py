# Generated by Django 3.0.1 on 2020-01-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20200101_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
    ]
