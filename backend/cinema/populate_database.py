from datetime import datetime

from django.utils.timezone import utc

from cinema.choices import MOVIE_GENRES
from cinema.models import *


def create_actors():
    Person.objects.bulk_create(
        [
            Person(name="Ana de Armas"),
            Person(
                name="Ben Affleck"
            ),
            Person(
                name="Jacob Elordi"
            ),
            Person(
                name="Finn Wittrock"
            ),
            Person(
                name="Rachel Blanchard"
            ),
            Person(
                name="Michael Keaton"
            ),
            Person(
                name="Michelle Pfeiffer"
            ),
            Person(
                name="Danny DeVito"
            ),
            Person(
                name="Christopher Walken"
            ),
            Person(
                name="Michael Gough"
            ),
            Person(
                name="Pat Hingle"
            ),
            Person(
                name="Jack Nicholson"
            ),
            Person(
                name="Kim Basinger"
            ),
            Person(
                name="Christian Bale"
            ),
            Person(
                name="Cillian Murphy"
            ),
            Person(
                name="Michael Caine"
            ),
            Person(
                name="Katie Holmes"
            ),
            Person(
                name="Liam Neeson"
            ),
            Person(
                name="Gary Oldman"
            ),
            Person(
                name="Morgan Freeman"
            ),
            Person(
                name="Heath Ledger"
            ),
            Person(
                name="Aaron Eckhart"
            ),
            Person(
                name="Tom Hardy"
            ),
            Person(
                name="Anne Hathaway"
            ),
            Person(
                name="Joseph Gordon-Levitt"
            ),
            Person(
                name="Marion Cotillard"
            ),
            Person(
                name="Brad Pitt"
            ),
            Person(
                name="Christoph Waltz"
            ),
            Person(
                name="Eli Roth"
            ),
            Person(
                name="Diane Kruger"
            ),
            Person(
                name="Mélanie Laurent"
            ),
            Person(
                name="Daniel Brühl"
            ),
            Person(
                name="Leonardo Dicaprio"
            ),
            Person(
                name="Margot Robbie"
            ),
            Person(
                name="Margaret Qualley"
            ),
            Person(
                name="Austin Butler"
            ),
            Person(
                name="Dakota Fanning"
            ),
            Person(
                name="Chris Evans"
            ),
            Person(
                name="Daniel Craig"
            ),
            Person(
                name="Jamie Lee Curtis"
            ),
            Person(
                name="Christopher Plummer"
            ),
            Person(
                name="Katherine Langford"
            ),
            Person(
                name="Mark Ruffalo"
            ),
            Person(
                name="Ben Kingsley"
            ),
            Person(
                name="Michelle Williams"
            ),
            Person(
                name="Max von Sydow"
            ),
            Person(
                name="Patricia Clarkson"
            ),
            Person(
                name="Robert De Niro"
            ),
            Person(
                name="Famke Janssen"
            ),
            Person(
                name="Jennifer Garner"
            ),
            Person(
                name="Christa B. Allen"
            ),
            Person(
                name="Judy Greer"
            ),
            Person(
                name="Andy Serkis"
            ),
            Person(
                name="Jennifer Lawrence"
            ),
            Person(
                name="Timothée Chalamet"
            ),
            Person(
                name="Cate Blanchett"
            ),
            Person(
                name="Meryl Streep"
            ),
            Person(
                name="Ariana Grande"
            ),
            Person(
                name="Ewan McGregor"
            ),
            Person(
                name="Albert Finney"
            ),
            Person(
                name="Helena Bonham Carter"
            ),
            Person(
                name="Billy Crudup"
            ),
            Person(
                name="Matthew McGrory"
            ),
        ]
    )


def create_directors():
    Person.objects.bulk_create(
        [
            Person(name="Adrian Lyne"),
            Person(name="Tim Burton"),
            Person(name="Christopher Nolan"),
            Person(name="Quentin Tarantino"),
            Person(name="Rian Johnson"),
            Person(name="Martin Scorsese"),
            Person(name="John Polson"),
            Person(name="Gary Winick"),
            Person(name="Adam McKay"),
        ]
    )


def create_movies():
    Movie.objects.bulk_create(
        [
            Movie(
                title="Deep Water",
                genre=MOVIE_GENRES.drama,
                release_date=datetime(2022, 4, 18, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=5.4,
                director=Person.objects.get(name="Adrian Lyne"),
            ),
            Movie(
                title="Batman",
                genre=MOVIE_GENRES.action,
                release_date=datetime(1989, 10, 26, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=7.5,
                director=Person.objects.get(name="Tim Burton"),
            ),
            Movie(
                title="Batman Returns",
                genre=MOVIE_GENRES.action,
                release_date=datetime(1992, 7, 3, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=7.1,
                director=Person.objects.get(name="Tim Burton"),
            ),
            Movie(
                title="Batman Begins",
                genre=MOVIE_GENRES.action,
                release_date=datetime(2005, 6, 17, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8.2,
                director=Person.objects.get(name="Christopher Nolan"),
            ),
            Movie(
                title="The Dark Knight",
                genre=MOVIE_GENRES.action,
                release_date=datetime(2008, 7, 18, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=9.0,
                director=Person.objects.get(name="Christopher Nolan"),
            ),
            Movie(
                title="The Dark Knight Rises",
                genre=MOVIE_GENRES.action,
                release_date=datetime(2012, 7, 27, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8.4,
                director=Person.objects.get(name="Christopher Nolan"),
            ),
            Movie(
                title="Inglourious Basterds",
                genre=MOVIE_GENRES.action,
                release_date=datetime(2009, 10, 9, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8.3,
                director=Person.objects.get(name="Quentin Tarantino"),
            ),
            Movie(
                title="Once Upon a Time in... Hollywood",
                genre=MOVIE_GENRES.comedy,
                release_date=datetime(2019, 8, 15, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=7.6,
                director=Person.objects.get(name="Quentin Tarantino"),
            ),
            Movie(
                title="Knives Out",
                genre=MOVIE_GENRES.mystery,
                release_date=datetime(2019, 12, 5, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=7.9,
                director=Person.objects.get(name="Rian Johnson"),
            ),
            Movie(
                title="Shutter Island",
                genre=MOVIE_GENRES.mystery,
                release_date=datetime(2010, 3, 12, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=8.2,
                director=Person.objects.get(name="Martin Scorsese"),
            ),
            Movie(
                title="Hide and Seek",
                genre=MOVIE_GENRES.mystery,
                release_date=datetime(2005, 1, 28, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=5.9,
                director=Person.objects.get(name="John Polson"),
            ),
            Movie(
                title="13 Going on 30",
                genre=MOVIE_GENRES.romance,
                release_date=datetime(2004, 4, 23, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=6.2,
                director=Person.objects.get(name="Gary Winick"),
            ),
            Movie(
                title="Don't Look Up",
                genre=MOVIE_GENRES.comedy,
                release_date=datetime(2021, 12, 9, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=7.2,
                director=Person.objects.get(name="Adam McKay"),
            ),
            Movie(
                title="Big Fish",
                genre=MOVIE_GENRES.fantasy,
                release_date=datetime(2004, 2, 20, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8,
                director=Person.objects.get(name="Tim Burton"),
            ),
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

    movie = Movie.objects.get(title="Batman")
    movie_cast = [
        Person.objects.get(name="Michael Keaton"),
        Person.objects.get(name="Jack Nicholson"),
        Person.objects.get(name="Kim Basinger"),
        Person.objects.get(name="Michael Gough"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Batman Returns")
    movie_cast = [
        Person.objects.get(name="Michael Keaton"),
        Person.objects.get(name="Michelle Pfeiffer"),
        Person.objects.get(name="Danny DeVito"),
        Person.objects.get(name="Christopher Walken"),
        Person.objects.get(name="Michael Gough"),
        Person.objects.get(name="Pat Hingle"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Batman Begins")
    movie_cast = [
        Person.objects.get(name="Christian Bale"),
        Person.objects.get(name="Cillian Murphy"),
        Person.objects.get(name="Michael Caine"),
        Person.objects.get(name="Katie Holmes"),
        Person.objects.get(name="Liam Neeson"),
        Person.objects.get(name="Gary Oldman"),
        Person.objects.get(name="Morgan Freeman"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="The Dark Knight")
    movie_cast = [
        Person.objects.get(name="Christian Bale"),
        Person.objects.get(name="Heath Ledger"),
        Person.objects.get(name="Gary Oldman"),
        Person.objects.get(name="Michael Caine"),
        Person.objects.get(name="Aaron Eckhart"),
        Person.objects.get(name="Morgan Freeman"),
        Person.objects.get(name="Cillian Murphy"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="The Dark Knight Rises")
    movie_cast = [
        Person.objects.get(name="Christian Bale"),
        Person.objects.get(name="Tom Hardy"),
        Person.objects.get(name="Anne Hathaway"),
        Person.objects.get(name="Joseph Gordon-Levitt"),
        Person.objects.get(name="Gary Oldman"),
        Person.objects.get(name="Marion Cotillard"),
        Person.objects.get(name="Michael Caine"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Inglourious Basterds")
    movie_cast = [
        Person.objects.get(name="Brad Pitt"),
        Person.objects.get(name="Christoph Waltz"),
        Person.objects.get(name="Eli Roth"),
        Person.objects.get(name="Quentin Tarantino"),
        Person.objects.get(name="Diane Kruger"),
        Person.objects.get(name="Mélanie Laurent"),
        Person.objects.get(name="Daniel Brühl"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Once Upon a Time in... Hollywood")
    movie_cast = [
        Person.objects.get(name="Brad Pitt"),
        Person.objects.get(name="Leonardo Dicaprio"),
        Person.objects.get(name="Margot Robbie"),
        Person.objects.get(name="Margaret Qualley"),
        Person.objects.get(name="Austin Butler"),
        Person.objects.get(name="Dakota Fanning"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Knives Out")
    movie_cast = [
        Person.objects.get(name="Chris Evans"),
        Person.objects.get(name="Ana de Armas"),
        Person.objects.get(name="Daniel Craig"),
        Person.objects.get(name="Jamie Lee Curtis"),
        Person.objects.get(name="Christopher Plummer"),
        Person.objects.get(name="Katherine Langford"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Shutter Island")
    movie_cast = [
        Person.objects.get(name="Leonardo Dicaprio"),
        Person.objects.get(name="Mark Ruffalo"),
        Person.objects.get(name="Ben Kingsley"),
        Person.objects.get(name="Michelle Williams"),
        Person.objects.get(name="Max von Sydow"),
        Person.objects.get(name="Patricia Clarkson"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Hide and Seek")
    movie_cast = [
        Person.objects.get(name="Dakota Fanning"),
        Person.objects.get(name="Robert De Niro"),
        Person.objects.get(name="Famke Janssen"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="13 Going on 30")
    movie_cast = [
        Person.objects.get(name="Jennifer Garner"),
        Person.objects.get(name="Mark Ruffalo"),
        Person.objects.get(name="Christa B. Allen"),
        Person.objects.get(name="Judy Greer"),
        Person.objects.get(name="Andy Serkis"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Don't Look Up")
    movie_cast = [
        Person.objects.get(name="Leonardo Dicaprio"),
        Person.objects.get(name="Jennifer Lawrence"),
        Person.objects.get(name="Timothée Chalamet"),
        Person.objects.get(name="Cate Blanchett"),
        Person.objects.get(name="Meryl Streep"),
        Person.objects.get(name="Ariana Grande"),
    ]
    movie.cast.set(movie_cast)

    movie = Movie.objects.get(title="Big Fish")
    movie_cast = [
        Person.objects.get(name="Ewan McGregor"),
        Person.objects.get(name="Albert Finney"),
        Person.objects.get(name="Helena Bonham Carter"),
        Person.objects.get(name="Billy Crudup"),
        Person.objects.get(name="Danny DeVito"),
        Person.objects.get(name="Matthew McGrory"),
    ]
    movie.cast.set(movie_cast)


def create_movies_nominations():
    Nomination.objects.bulk_create(
        [
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="The Dark Knight"),
                person=Person.objects.get(name="Heath Ledger"),
                category="Best Supporting Actor",
                year=2009,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="The Dark Knight"),
                person=Person.objects.get(name="Heath Ledger"),
                category="Best Performance by an Actor in a Supporting Role",
                year=2009,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                person=Person.objects.get(name="Jack Nicholson"),
                movie=Movie.objects.get(title="Batman"),
                category="Best Actor in a Supporting Role",
                year=1990,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="American Comedy Awards"),
                person=Person.objects.get(name="Jack Nicholson"),
                movie=Movie.objects.get(title="Batman"),
                category="Funniest Actor in a Motion Picture (Leading Role)",
                year=1990,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Inglourious Basterds"),
                person=Person.objects.get(name="Christoph Waltz"),
                category="Best Performance by an Actor in a Supporting Role",
                year=2010,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Inglourious Basterds"),
                person=Person.objects.get(name="Christoph Waltz"),
                category="Best Supporting Actor",
                year=2010,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Inglourious Basterds"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Director",
                year=2010,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Inglourious Basterds"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Screenplay - Original",
                year=2010,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Inglourious Basterds"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Achievement in Directing",
                year=2010,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Inglourious Basterds"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Writing, Original Screenplay",
                year=2010,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Once Upon a Time in... Hollywood"),
                person=Person.objects.get(name="Brad Pitt"),
                category="Best Performance by an Actor in a Supporting Role",
                year=2020,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Once Upon a Time in... Hollywood"),
                person=Person.objects.get(name="Brad Pitt"),
                category="Best Supporting Actor",
                year=2020,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Once Upon a Time in... Hollywood"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Motion Picture of the Year",
                year=2020,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Once Upon a Time in... Hollywood"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Achievement in Directing",
                year=2020,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Once Upon a Time in... Hollywood"),
                person=Person.objects.get(name="Quentin Tarantino"),
                category="Best Original Screenplay",
                year=2020,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Once Upon a Time in... Hollywood"),
                person=Person.objects.get(name="Leonardo Dicaprio"),
                category="Best Performance by an Actor in a Leading Role",
                year=2020,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="MTV Movie + TV Awards"),
                movie=Movie.objects.get(title="Hide and Seek"),
                person=Person.objects.get(name="Dakota Fanning"),
                category="Best Frightened Performance",
                year=2005,
                is_winner=True,
            ),
            Nomination(
                award=Award.objects.get(name="Academy Awards"),
                movie=Movie.objects.get(title="Don't Look Up"),
                person=Person.objects.get(name="Adam McKay"),
                category="Best Original Screenplay",
                year=2022,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Don't Look Up"),
                person=Person.objects.get(name="Adam McKay"),
                category="Best Screenplay (Original)",
                year=2022,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Don't Look Up"),
                person=Person.objects.get(name="Leonardo Dicaprio"),
                category="Best Leading Actor",
                year=2022,
                is_winner=False,
            ),
            Nomination(
                award=Award.objects.get(name="British Academy Film Awards"),
                movie=Movie.objects.get(title="Big Fish"),
                person=Person.objects.get(name="Albert Finney"),
                category="Best Performance by an Actor in a Supporting Role",
                year=2004,
                is_winner=False,
            ),
        ]
    )


def create_awards():
    Award.objects.bulk_create(
        [
            Award(name="Academy Awards"),
            Award(name="British Academy Film Awards"),
            Award(name="American Comedy Awards"),
            Award(name="MTV Movie + TV Awards"),
        ]
    )


def populate_database():
    Person.objects.all().delete()
    create_actors()
    create_directors()

    Movie.objects.all().delete()
    create_movies()
    create_movies_relations()

    Award.objects.all().delete()
    create_awards()

    Nomination.objects.all().delete()
    create_movies_nominations()
