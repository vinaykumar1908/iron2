# Generated by Django 3.0.5 on 2020-04-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROH', '0004_auto_20200424_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerhotaxle_wagon',
            name='WheelRecieveDate',
            field=models.DateField(),
        ),
    ]
