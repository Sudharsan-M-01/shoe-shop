# Generated by Django 3.2.10 on 2023-05-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_itemdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdb',
            name='productname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]