# Generated by Django 3.0.7 on 2020-06-24 16:56

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20200624_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 22, 26, 10, 166840)),
        ),
    ]
