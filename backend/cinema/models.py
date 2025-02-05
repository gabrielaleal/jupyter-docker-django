from django.db import models

from cinema.choices import MOVIE_GENRES


class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(choices=MOVIE_GENRES, max_length=255)
    release_date = models.DateField(null=True)
    cast = models.ManyToManyField(Person, related_name="movies_starred")
    director = models.ForeignKey(
        Person, related_name="movies_directed", null=True, on_delete=models.SET_NULL
    )
    imdb_rate = models.FloatField(null=True)

    def __str__(self):
        return f"{self.title}"


class Award(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.popular_name})"


class Nomination(models.Model):
    award = models.ForeignKey(Award, related_name="+", on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    year = models.IntegerField(null=True)
    is_winner = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, related_name="nominations", on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name="nominations", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.category} ({self.year}) - {self.award.name}"
