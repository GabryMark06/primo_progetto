# Generated by Django 5.1.3 on 2025-02-05 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_alter_articolo_data_articolo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='data_articolo',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 5, 11, 30, 41, 20919)),
        ),
        migrations.AlterField(
            model_name='giornalista',
            name='anno_nascita',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 5, 11, 30, 41, 20919)),
        ),
    ]
