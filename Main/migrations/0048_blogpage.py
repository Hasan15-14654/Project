# Generated by Django 5.1.1 on 2024-11-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0047_category_status_departments_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('banner', models.ImageField(upload_to='Blogs')),
                ('banner_head', models.CharField(max_length=200)),
                ('banner_description', models.TextField()),
            ],
        ),
    ]