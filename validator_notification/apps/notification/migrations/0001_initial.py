# Generated by Django 3.0.4 on 2020-03-09 22:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000, null=True)),
                ('img', models.CharField(max_length=1000, null=True)),
                ('notification_date', models.DateField(default=datetime.datetime(2020, 3, 9, 22, 8, 21, 495963, tzinfo=utc))),
            ],
        ),
    ]
