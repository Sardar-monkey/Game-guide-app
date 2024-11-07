# Generated by Django 5.1.2 on 2024-10-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=100, verbose_name='Game name')),
                ('gameimage', models.ImageField(upload_to='uploads/')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]