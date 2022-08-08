from django.db import models

from cinema.choices import MOVIE_GENRES


class Person(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)
    genre = models.CharField(choices=MOVIE_GENRES, max_length=255)
    release_date = models.DateField(null=True)
    is_available_on_netflix = models.BooleanField(default=False)
    imdb_rate = models.FloatField(null=True)
    cast = models.ManyToManyField(Person, related_name="movies_starred")
    director = models.ForeignKey(
        Person, related_name="movies_directed", null=True, on_delete=models.SET_NULL
    )
    budget = models.FloatField(null=True)


class Award(models.Model):
    name = models.CharField(max_length=255)
    popular_name = models.CharField(max_length=255, blank=True)
    first_presentation_date = models.DateField(null=True)


class Nomination(models.Model):
    award = models.ForeignKey(Award, related_name="+", on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    year = models.IntegerField(null=True)
    is_winner = models.BooleanField(default=False)

    class Meta:
        abstract = True


class MovieNomination(Nomination):
    movie = models.ForeignKey(Movie, related_name="nominations", on_delete=models.CASCADE)


class PersonNomination(Nomination):
    person = models.ForeignKey(Person, related_name="nominations", on_delete=models.CASCADE)
