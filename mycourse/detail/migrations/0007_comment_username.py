# Generated by Django 2.0.7 on 2018-07-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
