# Generated by Django 4.1.3 on 2022-11-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_User', '0004_alter_appuserprofile_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuserprofile',
            name='confirmation',
            field=models.CharField(default='D89I56+54J88-48V45745E', max_length=300, null=True),
        ),
    ]