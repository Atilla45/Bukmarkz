# Generated by Django 3.1.11 on 2022-08-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0002_auto_20211210_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
