# Generated by Django 5.1.1 on 2024-10-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0018_alter_billing_details_p_id_alter_cart_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='p_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
