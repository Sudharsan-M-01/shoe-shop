# Generated by Django 3.2.10 on 2023-05-24 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0003_cartdb_abouts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='images',
        ),
    ]
