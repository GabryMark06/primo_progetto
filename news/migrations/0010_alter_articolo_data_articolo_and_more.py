# Generated by Django 5.1.3 on 2025-01-29 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_articolo_data_articolo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='data_articolo',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 29, 9, 45, 16, 100901)),
        ),
        migrations.AlterField(
            model_name='giornalista',
            name='anno_nascita',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 29, 9, 45, 16, 100901)),
        ),
    ]
