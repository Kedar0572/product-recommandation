# Generated by Django 3.2.5 on 2021-08-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('asin', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('title', models.TextField(null=True)),
                ('product_type_name', models.TextField(null=True)),
                ('brand', models.TextField(null=True)),
                ('color', models.TextField(null=True)),
                ('formatted_price', models.TextField(null=True)),
                ('small_image_url', models.TextField(null=True)),
                ('medium_image_url', models.TextField(null=True)),
                ('large_image_url', models.TextField(null=True)),
            ],
        ),
    ]
