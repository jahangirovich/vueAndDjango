# Generated by Django 2.0.7 on 2018-07-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0018_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
