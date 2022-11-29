# Generated by Django 4.1.3 on 2022-11-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0020_remove_businesses_slug_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesses',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default="V63I75S59W85?76Q85#40'", max_length=300, null=True),
        ),
    ]
