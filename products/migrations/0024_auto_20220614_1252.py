# Generated by Django 3.2.13 on 2022-06-14 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20220614_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 6, 52, 17, 674704, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 6, 52, 17, 676138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='saubcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 6, 52, 17, 675476, tzinfo=utc)),
        ),
    ]
