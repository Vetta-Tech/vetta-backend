# Generated by Django 3.2.13 on 2022-06-11 21:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20220612_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 21, 59, 4, 628366, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 21, 59, 4, 628791, tzinfo=utc)),
        ),
    ]