# Generated by Django 3.2.13 on 2022-06-22 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220622_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalcart',
            name='total_saved',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 22, 41, 407715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 11, 22, 41, 408169, tzinfo=utc)),
        ),
    ]