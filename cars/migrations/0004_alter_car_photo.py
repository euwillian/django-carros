# Generated by Django 5.1.4 on 2025-01-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(upload_to='cars/'),
        ),
    ]