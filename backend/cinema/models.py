from django.db import models

from cinema.choices import MOVIE_GENRES


class Person(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True)
    death_date = models.DateTimeField(null=True)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    sinopsis = models.TextField()
    genre = models.CharField(choices=MOVIE_GENRES, max_length=255)
    release_date = models.DateTimeField(null=True)
    available_on_netflix = models.BooleanField(default=False)
    imdb_rate = models.FloatField()
    cast = models.ManyToManyField(Person, related_name="movies_starred")
    director = models.ForeignKey(
        Person, related_name="movies_directed", null=True, on_delete=models.SET_NULL
    )
    # budget


class Nomination(models.Model):
    award = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    year = models.IntegerField()
    winner = models.BooleanField(default=False)

    class Meta:
        abstract = True


class MovieNomination(Nomination):
    movie = models.ForeignKey(Movie, related_name="nominations", on_delete=models.CASCADE)


class PersonNomination(Nomination):
    person = models.ForeignKey(Person, related_name="nominations", on_delete=models.CASCADE)
