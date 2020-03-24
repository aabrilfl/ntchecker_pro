# Generated by Django 3.0.4 on 2020-03-23 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import validator_notification.apps.notification.utils.enumerations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualnotification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individualnotification',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='device.Device'),
        ),
        migrations.AddField(
            model_name='individualnotification',
            name='option_selected',
            field=models.CharField(choices=[('SI', 'OK'), ('NO', 'KO')], default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='individualnotification',
            name='status',
            field=models.CharField(choices=[('READ', 'READ'), ('NEW', 'NEW'), ('OPENED', 'OPENED')], default=validator_notification.apps.notification.utils.enumerations.status_notification['NEW'], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='individualnotification',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='generalnotification',
            name='thumbnail',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='generalnotification',
            name='url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='individualnotification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='individual_notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
