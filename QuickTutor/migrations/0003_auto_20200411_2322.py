# Generated by Django 3.0.2 on 2020-04-12 03:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0002_auto_20200411_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 4, 22, 42, 152429, tzinfo=utc)),
        ),
    ]
