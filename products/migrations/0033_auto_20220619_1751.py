# Generated by Django 3.2.13 on 2022-06-19 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20220619_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 19, 11, 51, 3, 811546, tzinfo=utc)),
        ),
    ]
