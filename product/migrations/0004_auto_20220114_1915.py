# Generated by Django 3.2 on 2022-01-14 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_picture_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
