# Generated by Django 3.0.4 on 2020-03-23 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_auto_20200323_0917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individualnotification',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]