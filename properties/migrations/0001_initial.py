# Generated by Django 3.2.7 on 2023-03-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projStatus', models.CharField(max_length=50, null=True)),
                ('propertyImage1', models.ImageField(blank=True, null=True, upload_to='')),
                ('propertyImage2', models.ImageField(blank=True, null=True, upload_to='')),
                ('propertyImage3', models.ImageField(blank=True, null=True, upload_to='')),
                ('projectName', models.CharField(max_length=50)),
                ('projectType', models.CharField(default=None, max_length=50)),
                ('projectStatus', models.CharField(default=None, max_length=50)),
                ('address', models.CharField(max_length=1100)),
                ('directions', models.URLField(default=None)),
                ('developmentSize', models.FloatField(default=None)),
                ('noOfUnits', models.IntegerField(default=None)),
                ('bedrooms', models.CharField(default=None, max_length=50)),
                ('about', models.TextField(default=None)),
                ('unitPlan1', models.ImageField(blank=True, upload_to='')),
                ('unitPlan2', models.ImageField(blank=True, upload_to='')),
                ('structure', models.TextField(default=None)),
                ('lobby', models.TextField(default=None)),
                ('lifts', models.TextField(default=None)),
                ('apartmentFlooring', models.TextField(default=None)),
                ('kitchen', models.TextField(default=None)),
                ('utility', models.TextField(default=None)),
                ('toiletsNFittings', models.TextField(default=None)),
                ('painting', models.TextField(default=None)),
                ('doorsNWindows', models.TextField(default=None)),
                ('electrical', models.TextField(default=None)),
                ('securitySystem', models.TextField(default=None)),
                ('dgBackup', models.TextField(default=None)),
            ],
        ),
    ]