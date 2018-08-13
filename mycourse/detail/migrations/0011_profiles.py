# Generated by Django 2.0.7 on 2018-07-29 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0010_auto_20180729_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('firstName', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
