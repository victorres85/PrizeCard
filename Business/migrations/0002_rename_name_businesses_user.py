# Generated by Django 4.1.3 on 2022-11-08 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesses',
            old_name='name',
            new_name='user',
        ),
    ]