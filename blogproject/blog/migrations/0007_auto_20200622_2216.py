# Generated by Django 3.0.3 on 2020-06-22 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200622_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 16, 46, 38, 766826, tzinfo=utc)),
        ),
    ]
