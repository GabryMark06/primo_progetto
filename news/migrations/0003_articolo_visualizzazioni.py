# Generated by Django 5.1.3 on 2025-01-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articolo_options_alter_giornalista_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='articolo',
            name='visualizzazioni',
            field=models.IntegerField(db_default=0),
        ),
    ]
