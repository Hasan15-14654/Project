# Generated by Django 5.1.1 on 2024-10-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0019_delivery_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='p_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
