# Generated by Django 3.2.13 on 2022-06-14 05:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('products', '0022_auto_20220612_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 5, 13, 51, 482981, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 14, 5, 13, 51, 484301, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='SaubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='image/subcategory')),
                ('status', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 6, 14, 5, 13, 51, 483684, tzinfo=utc))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name_plural': 'Subcategory',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.saubcategory'),
        ),
    ]