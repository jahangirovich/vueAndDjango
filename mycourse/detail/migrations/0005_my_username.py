# Generated by Django 2.0.7 on 2018-07-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0004_auto_20180726_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='my',
            name='username',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
