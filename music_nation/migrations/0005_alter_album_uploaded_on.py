# Generated by Django 4.1.4 on 2024-02-10 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0004_auto_20181004_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2024, 2, 10, 19, 39, 28, 151403)),
        ),
    ]
