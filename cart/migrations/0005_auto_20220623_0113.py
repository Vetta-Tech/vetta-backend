# Generated by Django 3.2.13 on 2022-06-22 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20220623_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 13, 29, 2074, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 13, 29, 2606, tzinfo=utc)),
        ),
    ]