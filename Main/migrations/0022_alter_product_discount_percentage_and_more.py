# Generated by Django 5.1.1 on 2024-10-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0021_product_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
