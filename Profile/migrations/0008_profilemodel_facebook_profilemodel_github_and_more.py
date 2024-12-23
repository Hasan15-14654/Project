# Generated by Django 5.1.1 on 2024-11-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_profilemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='facebook',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='instagram',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='linkedin',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='telegram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='twitter',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
