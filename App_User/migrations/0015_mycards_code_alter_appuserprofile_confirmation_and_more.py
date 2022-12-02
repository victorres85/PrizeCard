# Generated by Django 4.1.3 on 2022-11-30 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Business', '0047_alter_profile_confirmation'),
        ('App_User', '0014_mycards_image_alter_appuserprofile_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycards',
            name='code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='appuserprofile',
            name='confirmation',
            field=models.CharField(default="'43<70G62N54/74N64:568", max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mycards',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/app_user/'),
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_key', models.CharField(max_length=300, unique=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Business.cards')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
