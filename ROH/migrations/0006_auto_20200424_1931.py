# Generated by Django 3.0.5 on 2020-04-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROH', '0005_auto_20200424_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerhotaxle_wagon',
            name='DateDetached',
            field=models.DateField(blank=True),
        ),
    ]