# Generated by Django 4.1.3 on 2022-11-26 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_User', '0005_alter_appuserprofile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuserprofile',
            name='confirmation',
            field=models.CharField(default='T71N46:41E42L34348X44P', max_length=300, null=True),
        ),
    ]
