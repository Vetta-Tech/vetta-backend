# Generated by Django 3.2.13 on 2022-06-24 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0017_auto_20220624_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 14, 13, 39, 151497, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 24, 14, 13, 39, 152289, tzinfo=utc)),
        ),
    ]
