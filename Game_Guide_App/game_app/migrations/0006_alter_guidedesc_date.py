# Generated by Django 5.1.2 on 2024-10-30 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0005_remove_guidedesc_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guidedesc',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date'),
        ),
    ]