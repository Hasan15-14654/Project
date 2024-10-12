# Generated by Django 5.1.1 on 2024-10-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_alter_homecarousel_link_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing_details',
            name='state',
        ),
        migrations.AddField(
            model_name='billing_details',
            name='Street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='billing_details',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='billing_details',
            name='order_note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]