# Generated by Django 3.2 on 2022-01-18 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_auto_20220118_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users_wishlist',
            field=models.ManyToManyField(blank=True, related_name='users_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
