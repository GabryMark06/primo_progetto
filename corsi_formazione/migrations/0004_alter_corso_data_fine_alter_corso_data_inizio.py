# Generated by Django 5.1.3 on 2025-03-19 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corsi_formazione', '0003_alter_corso_data_fine_alter_corso_data_inizio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corso',
            name='data_fine',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 19, 11, 18, 32, 557735)),
        ),
        migrations.AlterField(
            model_name='corso',
            name='data_inizio',
            field=models.DateTimeField(default=datetime.datetime(2025, 3, 19, 11, 18, 32, 557735)),
        ),
    ]
