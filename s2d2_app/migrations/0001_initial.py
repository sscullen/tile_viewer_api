# Generated by Django 2.2 on 2019-04-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shapefile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('shp_shp', models.FileField(upload_to='shapefiles/')),
                ('shp_dbf', models.FileField(upload_to='shapefiles/')),
                ('shp_shx', models.FileField(upload_to='shapefiles/')),
                ('shp_prj', models.FileField(upload_to='shapefiles/')),
                ('shp_xml', models.FileField(blank=True, upload_to='shapefiles/')),
                ('shp_sbx', models.FileField(blank=True, upload_to='shapefiles/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
