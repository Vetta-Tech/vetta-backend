# Generated by Django 3.2.13 on 2022-06-11 22:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20220612_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 22, 3, 32, 665370, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 11, 22, 3, 32, 666158, tzinfo=utc)),
        ),
    ]
