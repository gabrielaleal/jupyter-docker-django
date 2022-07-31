from datetime import datetime
from venv import create

from django.utils.timezone import utc

from cinema.choices import MOVIE_GENRES
from cinema.models import *


def create_actors():
    Person.objects.bulk_create(
        [
            Person(
                name="Ana de Armas", birth_date=datetime(1988, 4, 30, 3, 59, 0, 99999, tzinfo=utc)
            ),
            Person(
                name="Ben Affleck", birth_date=datetime(1972, 8, 15, 3, 59, 0, 99999, tzinfo=utc)
            ),
            Person(
                name="Jacob Elordi", birth_date=datetime(1997, 6, 26, 3, 59, 0, 99999, tzinfo=utc)
            ),
            Person(
                name="Finn Wittrock", birth_date=datetime(1984, 10, 28, 3, 59, 0, 99999, tzinfo=utc)
            ),
            Person(
                name="Rachel Blanchard",
                birth_date=datetime(1976, 3, 19, 3, 59, 0, 99999, tzinfo=utc),
            ),
        ]
    )


def create_directors():
    Person.objects.bulk_create(
        [
            Person(
                name="Adrian Lyne", birth_date=datetime(1941, 3, 4, 3, 59, 0, 99999, tzinfo=utc)
            ),
        ]
    )


def create_movies():
    Movie.objects.bulk_create(
        [
            Movie(
                title="Deep Water",
                sinopsis=(
                    "Vic and Melinda, a married couple, fall out of love with each other and the "
                    "latter pursues extramarital affairs. However, when her lovers all disappear, "
                    "the suspicion falls on Vic."
                ),
                genre=MOVIE_GENRES.drama,
                release_date=datetime(2022, 4, 18, 3, 59, 0, 99999, tzinfo=utc),
                available_on_netflix=False,
                imdb_rate=5.4,
                director=Person.objects.get(name="Adrian Lyne"),
            )
        ]
    )


def create_movies_relations():
    movie = Movie.objects.get(title="Deep Water")
    movie_cast = [
        Person.objects.get(name="Ana de Armas"),
        Person.objects.get(name="Ben Affleck"),
        Person.objects.get(name="Jacob Elordi"),
        Person.objects.get(name="Finn Wittrock"),
        Person.objects.get(name="Rachel Blanchard"),
    ]
    movie.cast.set(movie_cast)


def create_movies_nominations():
    ...


def create_people_nominations():
    ...


def populate_database():
    Person.objects.all().delete()
    create_actors()
    create_directors()

    Movie.objects.all().delete()
    create_movies()
    create_movies_relations()
