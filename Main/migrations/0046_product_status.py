# Generated by Django 5.1.1 on 2024-11-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0045_alter_blogpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
