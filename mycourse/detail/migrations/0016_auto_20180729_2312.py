# Generated by Django 2.0.7 on 2018-07-29 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0015_remove_hi_friends'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hi',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, to='detail.Profiles'),
            preserve_default=False,
        ),
    ]