# Generated by Django 3.2.13 on 2022-06-22 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_auto_20220622_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 10, 34, 27, 284957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 10, 34, 27, 285785, tzinfo=utc)),
        ),
    ]
