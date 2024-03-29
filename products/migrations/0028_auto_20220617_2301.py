# Generated by Django 3.2.13 on 2022-06-17 17:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_supplier_category'),
        ('category', '0001_initial'),
        ('products', '0027_auto_20220617_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='keywords',
        ),
        migrations.AddField(
            model_name='products',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 17, 1, 33, 965926, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.subcategory'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
