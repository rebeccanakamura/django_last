# Generated by Django 2.2.6 on 2019-11-01 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20191101_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_badge',
            field=models.CharField(choices=[('none', 'NONE'), ('special', 'SPECIAL')], default='NONE', max_length=20),
        ),
    ]