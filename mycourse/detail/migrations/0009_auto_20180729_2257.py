# Generated by Django 2.0.7 on 2018-07-29 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0008_auto_20180729_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfriends',
            name='friends',
        ),
        migrations.DeleteModel(
            name='MyFriends',
        ),
    ]
