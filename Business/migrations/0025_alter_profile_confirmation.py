# Generated by Django 4.1.3 on 2022-11-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0024_profile_slug_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='489M56676C50+82%50@91=', max_length=300, null=True),
        ),
    ]