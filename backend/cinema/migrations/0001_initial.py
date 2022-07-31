# Generated by Django 3.2.14 on 2022-07-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sinopsis', models.TextField()),
                ('genre', models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('mistery', 'Mistery'), ('romance', 'Romance'), ('thriller', 'Thriller'), ('science_fiction', 'Science-Fiction')], max_length=255)),
                ('release_date', models.DateTimeField(null=True)),
                ('available_on_netflix', models.BooleanField(default=False)),
                ('imdb_rate', models.FloatField()),
            ],
        ),
    ]
