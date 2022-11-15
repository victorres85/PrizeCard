# Generated by Django 4.1.3 on 2022-11-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0015_alter_businesses_slug_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default=')67/42F91=65140862W60:', max_length=300, null=True),
        ),
    ]
