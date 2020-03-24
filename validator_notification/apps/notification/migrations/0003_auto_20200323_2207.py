# Generated by Django 3.0.4 on 2020-03-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20200323_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualnotification',
            name='status',
            field=models.CharField(choices=[('READ', 'READ'), ('NEW', 'NEW'), ('OPENED', 'OPENED')], default='NEW', max_length=50, null=True),
        ),
    ]
