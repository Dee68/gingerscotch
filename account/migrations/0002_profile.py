# Generated by Django 3.2 on 2022-01-02 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, default='/userimage.png', upload_to='profile_pics/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
