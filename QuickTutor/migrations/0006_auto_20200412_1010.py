# Generated by Django 3.0.2 on 2020-04-12 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0005_auto_20200412_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 16, 10, 28, 548752, tzinfo=utc)),
        ),
    ]
