# Generated by Django 3.2 on 2022-02-05 20:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_manager_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]