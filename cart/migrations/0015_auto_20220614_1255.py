# Generated by Django 3.2.13 on 2022-06-14 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20220614_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 6, 55, 55, 900811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 6, 55, 55, 901319, tzinfo=utc)),
        ),
    ]
