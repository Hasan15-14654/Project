# Generated by Django 5.1.1 on 2024-10-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='p_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
