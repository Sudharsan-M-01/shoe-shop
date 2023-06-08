# Generated by Django 4.1.6 on 2023-05-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Categoryname', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.CharField(blank=True, max_length=100, null=True)),
                ('Size', models.CharField(blank=True, max_length=100, null=True)),
                ('Color', models.CharField(blank=True, max_length=100, null=True)),
                ('Type', models.CharField(blank=True, max_length=100, null=True)),
                ('About', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
