# Generated by Django 3.0.4 on 2020-04-27 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_device_onesignal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='tlf',
            field=models.CharField(default=123456789, max_length=50),
            preserve_default=False,
        ),
    ]
