# Generated by Django 4.1.3 on 2022-11-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0034_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='I68%65S57V52B90360=86)', max_length=300, null=True),
        ),
    ]
