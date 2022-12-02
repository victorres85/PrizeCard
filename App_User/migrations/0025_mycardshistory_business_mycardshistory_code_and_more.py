# Generated by Django 4.1.3 on 2022-12-02 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0058_alter_profile_confirmation'),
        ('App_User', '0024_alter_appuserprofile_confirmation'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycardshistory',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Business.businesses'),
        ),
        migrations.AddField(
            model_name='mycardshistory',
            name='code',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='appuserprofile',
            name='confirmation',
            field=models.CharField(default='I38E91&74F40A58M71764D', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mycardshistory',
            name='card',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Business.cards'),
        ),
    ]
