# Generated by Django 5.1.1 on 2024-10-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_brand_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('banner', models.ImageField(upload_to='Project')),
            ],
        ),
    ]
