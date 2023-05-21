# Generated by Django 4.1 on 2023-02-07 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=25)),
                ('text', models.TextField(default='', max_length=100)),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 2, 7, 7, 29, 5, 933088, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
