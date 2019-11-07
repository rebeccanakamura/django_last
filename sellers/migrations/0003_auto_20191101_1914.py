# Generated by Django 2.2.6 on 2019-11-01 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_seller_item_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_address_1',
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_address_2',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_city',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_email',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_phone',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_state',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='seller',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]