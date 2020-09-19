# Generated by Django 2.1.7 on 2019-02-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('2', 'Medium'), ('1', 'High')], default='L', max_length=1),
        ),
    ]
