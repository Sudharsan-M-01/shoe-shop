# Generated by Django 3.2.10 on 2023-05-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0013_customerdetails_confirmpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Towncity', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, max_length=100, null=True)),
                ('Emailaddress', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
