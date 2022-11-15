# Generated by Django 4.1.3 on 2022-11-15 13:24

import Business.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0018_alter_businesses_slug_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='slug',
            field=models.SlugField(blank=True, default=Business.models.confirmation_code, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default="C67076L60F58R50154790'", max_length=300, null=True),
        ),
    ]
