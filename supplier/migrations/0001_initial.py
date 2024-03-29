# Generated by Django 3.2.13 on 2022-06-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0027_auto_20220617_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('descrition', models.TextField(blank=True, max_length=300, null=True)),
                ('logo', models.ImageField(upload_to='images/brand/logo')),
                ('cover_image', models.ImageField(upload_to='images/brand/cover')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='products.Category')),
            ],
        ),
    ]
