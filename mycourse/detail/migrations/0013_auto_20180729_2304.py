# Generated by Django 2.0.7 on 2018-07-29 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0012_myfriends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myfriends',
            old_name='friend',
            new_name='friends',
        ),
    ]
