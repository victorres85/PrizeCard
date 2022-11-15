# Generated by Django 4.1.3 on 2022-11-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0023_remove_profile_slug_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='Q87&91/68@79247:80W57@', max_length=300, null=True),
        ),
    ]
