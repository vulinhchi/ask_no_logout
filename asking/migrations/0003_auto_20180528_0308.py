# Generated by Django 2.0.5 on 2018-05-28 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asking', '0002_auto_20180528_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='asking_day',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
