# Generated by Django 3.2.13 on 2022-06-19 11:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20220619_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 19, 11, 42, 32, 920281, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 19, 11, 42, 32, 920974, tzinfo=utc)),
        ),
    ]
