# Generated by Django 4.1.3 on 2022-11-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0049_alter_profile_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='confirmation',
            field=models.CharField(default='N42<59Z42*70/59V66;538', max_length=300, null=True),
        ),
    ]
