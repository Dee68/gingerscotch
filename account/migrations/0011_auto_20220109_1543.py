# Generated by Django 3.2 on 2022-01-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20220109_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_type',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user_type',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]