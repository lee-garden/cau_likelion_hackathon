# Generated by Django 2.2.1 on 2019-05-24 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cau_quiz', '0006_auto_20190524_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pub_date_1',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 23, 40, 19, 99883), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='player',
            name='pub_date_2',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 23, 40, 19, 99883), verbose_name='date published'),
        ),
    ]
