# Generated by Django 4.1.3 on 2022-11-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0005_businesses_slug_cards_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesses',
            name='email',
        ),
        migrations.AlterField(
            model_name='businesses',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='address_first_line',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='post_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='businesses',
            name='region',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
