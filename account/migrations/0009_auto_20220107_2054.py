# Generated by Django 3.2 on 2022-01-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20220107_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_manager',
        ),
    ]