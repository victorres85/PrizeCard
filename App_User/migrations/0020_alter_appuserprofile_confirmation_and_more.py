# Generated by Django 4.1.3 on 2022-11-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_User', '0019_alter_appuserprofile_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuserprofile',
            name='confirmation',
            field=models.CharField(default='@71Z46-86875P76R74?736', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='appuserprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='app_user'),
        ),
    ]
