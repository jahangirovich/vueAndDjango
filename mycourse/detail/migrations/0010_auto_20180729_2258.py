# Generated by Django 2.0.7 on 2018-07-29 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0009_auto_20180729_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]