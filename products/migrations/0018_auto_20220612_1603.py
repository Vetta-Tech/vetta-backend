# Generated by Django 3.2.13 on 2022-06-12 10:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20220612_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 10, 3, 20, 958707, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 12, 10, 3, 20, 959596, tzinfo=utc)),
        ),
    ]