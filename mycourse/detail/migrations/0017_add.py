# Generated by Django 2.0.7 on 2018-07-30 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0016_auto_20180729_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detail.Profiles')),
            ],
        ),
    ]
