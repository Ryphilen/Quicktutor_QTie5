# Generated by Django 3.0.2 on 2020-03-02 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='course_num',
            field=models.IntegerField(default='0000'),
        ),
    ]
