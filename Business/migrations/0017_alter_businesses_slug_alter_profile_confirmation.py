# Generated by Django 4.1.3 on 2022-11-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0016_alter_businesses_slug_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='$75W71M59C87V71172<762', max_length=300, null=True),
        ),
    ]