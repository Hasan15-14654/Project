# Generated by Django 5.1.1 on 2024-10-27 17:10

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0034_order_delivery_charge'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('division', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=100)),
                ('thana', models.CharField(max_length=100)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(max_length=25)),
                ('order_note', models.CharField(blank=True, max_length=200, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('second_phone', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=50.0, max_digits=10)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='Main.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]