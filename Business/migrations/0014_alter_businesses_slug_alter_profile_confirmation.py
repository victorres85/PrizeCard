# Generated by Django 4.1.3 on 2022-11-15 13:21

import Business.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0013_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='slug',
            field=models.SlugField(blank=True, default=Business.models.confirmation_code, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='A57055B88%82S76D78457L', max_length=300, null=True),
        ),
    ]
