# Generated by Django 3.2 on 2022-08-21 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('mystery', 'Mystery'), ('romance', 'Romance'), ('thriller', 'Thriller'), ('science_fiction', 'Science-Fiction')], max_length=255)),
                ('release_date', models.DateField(null=True)),
                ('is_available_on_netflix', models.BooleanField(default=False)),
                ('imdb_rate', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('year', models.IntegerField(null=True)),
                ('is_winner', models.BooleanField(default=False)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cinema.award')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nominations', to='cinema.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nominations', to='cinema.person')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(related_name='movies_starred', to='cinema.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies_directed', to='cinema.person'),
        ),
    ]
