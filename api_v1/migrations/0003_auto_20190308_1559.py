# Generated by Django 2.1.7 on 2019-03-08 15:59

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_auto_20190220_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='paused',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='schedule',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='worker',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
