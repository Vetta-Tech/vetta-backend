# Generated by Django 3.2.13 on 2022-06-25 19:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20220624_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 19, 40, 4, 484767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 25, 19, 40, 4, 485303, tzinfo=utc)),
        ),
    ]
