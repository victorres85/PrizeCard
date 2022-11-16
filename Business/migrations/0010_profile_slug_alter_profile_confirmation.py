# Generated by Django 4.1.3 on 2022-11-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0009_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='+44743M35N47-75G68644V', max_length=300, null=True),
        ),
    ]