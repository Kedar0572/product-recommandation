# Generated by Django 3.2.5 on 2021-08-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(null=True),
        ),
    ]