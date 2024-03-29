# Generated by Django 3.2.13 on 2022-06-22 10:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 10, 39, 30, 418415, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coupon.coupon'),
        ),
        migrations.AlterField(
            model_name='finalcart',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 10, 39, 30, 418993, tzinfo=utc)),
        ),
    ]
