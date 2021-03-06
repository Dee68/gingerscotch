# Generated by Django 3.2 on 2022-01-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20220110_1909'),
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
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('customer', 'CUSTOMER'), ('manager', 'MANAGER')], default='', max_length=10),
        ),
    ]
