# Generated by Django 2.0.6 on 2018-07-25 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_desc',
            field=models.TextField(default=datetime.datetime(2018, 7, 25, 17, 38, 7, 624975, tzinfo=utc)),
            preserve_default=False,
        ),
    ]