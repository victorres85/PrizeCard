# Generated by Django 4.1.3 on 2022-11-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0040_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='052J80%75@85158553C660', max_length=300, null=True),
        ),
    ]