# Generated by Django 5.1.1 on 2024-10-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0017_billing_details_p_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_details',
            name='p_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='p_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]