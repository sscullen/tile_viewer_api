# Generated by Django 2.2.5 on 2019-09-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0004_auto_20190309_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='priority',
            field=models.CharField(choices=[('3', 'LOW'), ('2', 'MEDIUM'), ('1', 'HIGH')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('S', 'SUBMITTED'), ('A', 'ASSIGNED'), ('C', 'COMPLETED')], default='S', max_length=1),
        ),
    ]
