# Generated by Django 2.2.5 on 2019-09-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20190916_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
    ]
