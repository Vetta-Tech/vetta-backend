# Generated by Django 3.2.13 on 2022-06-24 14:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0016_auto_20220623_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 14, 11, 38, 830550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 14, 11, 38, 831264, tzinfo=utc)),
        ),
    ]
