# Generated by Django 3.2.10 on 2023-05-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0011_newcartdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcartdb',
            name='userr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
