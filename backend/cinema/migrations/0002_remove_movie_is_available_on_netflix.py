# Generated by Django 3.2 on 2022-08-21 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_available_on_netflix',
        ),
    ]
