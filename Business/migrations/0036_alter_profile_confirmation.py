# Generated by Django 4.1.3 on 2022-11-26 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0035_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='745565J69671G42$448373', max_length=300, null=True),
        ),
    ]