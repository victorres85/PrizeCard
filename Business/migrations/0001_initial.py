# Generated by Django 4.1.3 on 2022-11-08 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Businesses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('address_first_line', models.CharField(max_length=200)),
                ('address_second_line', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=10)),
                ('phone_number', models.IntegerField()),
                ('logo', models.ImageField(blank=True, upload_to='media/businesses/%y/%m/%d')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('total_points', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Business.businesses')),
            ],
        ),
    ]
