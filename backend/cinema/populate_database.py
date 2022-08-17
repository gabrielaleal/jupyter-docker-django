from datetime import datetime

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
            Person(
                name="Michael Keaton",
                birth_date=datetime(1951, 9, 5, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Michelle Pfeiffer",
                birth_date=datetime(1958, 4, 29, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Danny DeVito",
                birth_date=datetime(1944, 11, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Christopher Walken",
                birth_date=datetime(1943, 3, 31, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Michael Gough",
                birth_date=datetime(1916, 11, 23, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2011, 3, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Pat Hingle",
                birth_date=datetime(1924, 7, 19, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2009, 1, 3, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Jack Nicholson",
                birth_date=datetime(1937, 4, 22, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Kim Basinger",
                birth_date=datetime(1953, 12, 8, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Christian Bale",
                birth_date=datetime(1974, 1, 30, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Cillian Murphy",
                birth_date=datetime(1976, 5, 25, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Michael Caine",
                birth_date=datetime(1933, 3, 14, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Katie Holmes",
                birth_date=datetime(1978, 12, 18, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Liam Neeson",
                birth_date=datetime(1952, 6, 7, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Gary Oldman",
                birth_date=datetime(1958, 3, 21, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Morgan Freeman",
                birth_date=datetime(1937, 6, 1, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Heath Ledger",
                birth_date=datetime(1979, 4, 4, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2008, 1, 22, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Aaron Eckhart",
                birth_date=datetime(1968, 1, 12, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Tom Hardy",
                birth_date=datetime(1977, 9, 15, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Anne Hathaway",
                birth_date=datetime(1982, 11, 12, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Joseph Gordon-Levitt",
                birth_date=datetime(1981, 2, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Marion Cotillard",
                birth_date=datetime(1975, 9, 30, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Brad Pitt",
                birth_date=datetime(1963, 12, 18, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Christoph Waltz",
                birth_date=datetime(1956, 10, 4, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Eli Roth",
                birth_date=datetime(1972, 4, 18, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Diane Kruger",
                birth_date=datetime(1976, 7, 15, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Mélanie Laurent",
                birth_date=datetime(1983, 2, 21, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Daniel Brühl",
                birth_date=datetime(1978, 6, 16, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Leonardo Dicaprio",
                birth_date=datetime(1974, 11, 11, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Margot Robbie",
                birth_date=datetime(1990, 7, 2, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Margaret Qualley",
                birth_date=datetime(1994, 10, 23, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Austin Butler",
                birth_date=datetime(1991, 8, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Dakota Fanning",
                birth_date=datetime(1994, 2, 23, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Chris Evans",
                birth_date=datetime(1981, 6, 13, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Daniel Craig",
                birth_date=datetime(1968, 3, 2, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Jamie Lee Curtis",
                birth_date=datetime(1958, 11, 22, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Christopher Plummer",
                birth_date=datetime(1929, 12, 13, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Katherine Langford",
                birth_date=datetime(1996, 4, 29, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Mark Ruffalo",
                birth_date=datetime(1967, 11, 22, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Ben Kingsley",
                birth_date=datetime(1943, 12, 31, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Michelle Williams",
                birth_date=datetime(1980, 9, 9, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Max von Sydow",
                birth_date=datetime(1929, 4, 10, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2020, 3, 8, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Patricia Clarkson",
                birth_date=datetime(1959, 12, 29, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Robert De Niro",
                birth_date=datetime(1943, 8, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Famke Janssen",
                birth_date=datetime(1964, 11, 5, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Jennifer Garner",
                birth_date=datetime(1972, 4, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Christa B. Allen",
                birth_date=datetime(1991, 11, 11, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Judy Greer",
                birth_date=datetime(1975, 7, 20, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Andy Serkis",
                birth_date=datetime(1964, 4, 20, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Jennifer Lawrence",
                birth_date=datetime(1990, 8, 15, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Timothée Chalamet",
                birth_date=datetime(1995, 12, 27, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Cate Blanchett",
                birth_date=datetime(1969, 5, 14, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Meryl Streep",
                birth_date=datetime(1949, 6, 22, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Ariana Grande",
                birth_date=datetime(1993, 6, 26, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Ewan McGregor",
                birth_date=datetime(1971, 3, 31, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Albert Finney",
                birth_date=datetime(1936, 5, 9, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2019, 2, 7, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Helena Bonham Carter",
                birth_date=datetime(1966, 5, 26, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Billy Crudup",
                birth_date=datetime(1968, 7, 8, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Matthew McGrory",
                birth_date=datetime(1973, 5, 17, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2005, 8, 9, 3, 59, 0, 99999, tzinfo=utc),
            ),
        ]
    )


def create_directors():
    Person.objects.bulk_create(
        [
            Person(
                name="Adrian Lyne", birth_date=datetime(1941, 3, 4, 3, 59, 0, 99999, tzinfo=utc)
            ),
            Person(
                name="Tim Burton", birth_date=datetime(1958, 8, 25, 3, 59, 0, 99999, tzinfo=utc)
            ),
            Person(
                name="Christopher Nolan",
                birth_date=datetime(1970, 7, 30, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Quentin Tarantino",
                birth_date=datetime(1963, 3, 27, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Rian Johnson",
                birth_date=datetime(1973, 12, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Martin Scorsese",
                birth_date=datetime(1942, 11, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="John Polson",
                birth_date=datetime(1965, 9, 6, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Gary Winick",
                birth_date=datetime(1961, 3, 31, 3, 59, 0, 99999, tzinfo=utc),
                death_date=datetime(2011, 2, 27, 3, 59, 0, 99999, tzinfo=utc),
            ),
            Person(
                name="Adam McKay",
                birth_date=datetime(1968, 4, 17, 3, 59, 0, 99999, tzinfo=utc),
            ),
        ]
    )


def create_movies():
    Movie.objects.bulk_create(
        [
            Movie(
                title="Deep Water",
                synopsis=(
                    "Vic and Melinda, a married couple, fall out of love with each other and the "
                    "latter pursues extramarital affairs. However, when her lovers all disappear, "
                    "the suspicion falls on Vic."
                ),
                genre=MOVIE_GENRES.drama,
                release_date=datetime(2022, 4, 18, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=5.4,
                director=Person.objects.get(name="Adrian Lyne"),
            ),
            Movie(
                title="Batman",
                synopsis=(
                    "When Max, an entrepreneur, and criminal Penguin team up to wreak havoc in "
                    "Gotham City, Batman decides to stop them. Catwoman's alter ego, Selina Kyle, "
                    "seeks revenge on Max for trying to kill her."
                ),
                genre=MOVIE_GENRES.action,
                release_date=datetime(1989, 10, 26, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=7.5,
                director=Person.objects.get(name="Tim Burton"),
            ),
            Movie(
                title="Batman Returns",
                synopsis=(
                    "When Max, an entrepreneur, and criminal Penguin team up to wreak havoc in "
                    "Gotham City, Batman decides to stop them. Catwoman's alter ego, Selina Kyle, "
                    "seeks revenge on Max for trying to kill her."
                ),
                genre=MOVIE_GENRES.action,
                release_date=datetime(1992, 7, 3, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=7.1,
                director=Person.objects.get(name="Tim Burton"),
            ),
            Movie(
                title="Batman Begins",
                synopsis=(
                    "After witnessing his parents' death, Bruce learns the art of fighting to "
                    "confront injustice. When he returns to Gotham as Batman, he must stop a secret"
                    " society that intends to destroy the city."
                ),
                genre=MOVIE_GENRES.action,
                release_date=datetime(2005, 6, 17, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8.2,
                director=Person.objects.get(name="Christopher Nolan"),
            ),
            Movie(
                title="The Dark Knight",
                synopsis=(
                    "After Gordon, Dent and Batman begin an assault on Gotham's organised crime, "
                    "the mobs hire the Joker, a psychopathic criminal mastermind who offers to kill"
                    " Batman and bring the city to its knees."
                ),
                genre=MOVIE_GENRES.action,
                release_date=datetime(2008, 7, 18, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=9.0,
                director=Person.objects.get(name="Christopher Nolan"),
            ),
            Movie(
                title="The Dark Knight Rises",
                synopsis=(
                    "Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-"
                    "long period of peace. This forces Bruce Wayne to come out of hiding and don "
                    "the cape and cowl of Batman again."
                ),
                genre=MOVIE_GENRES.action,
                release_date=datetime(2012, 7, 27, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8.4,
                director=Person.objects.get(name="Christopher Nolan"),
            ),
            Movie(
                title="Inglourious Basterds",
                synopsis=(
                    "A few Jewish soldiers are on an undercover mission to bring down the Nazi "
                    "government and put an end to the war. Meanwhile, a woman wants to avenge the "
                    "death of her family from a German officer."
                ),
                genre=MOVIE_GENRES.action,
                release_date=datetime(2009, 10, 9, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=8.3,
                director=Person.objects.get(name="Quentin Tarantino"),
            ),
            Movie(
                title="Once Upon a Time in... Hollywood",
                synopsis=(
                    "Rick, a washed-out actor, and Cliff, his stunt double, struggle to recapture "
                    "fame and success in 1960s Los Angeles. Meanwhile, living next door to Rick is "
                    "Sharon Tate and her husband Roman Polanski."
                ),
                genre=MOVIE_GENRES.comedy,
                release_date=datetime(2019, 8, 15, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=7.6,
                director=Person.objects.get(name="Quentin Tarantino"),
            ),
            Movie(
                title="Knives Out",
                synopsis=(
                    "Harlan Thrombey, a reputable crime novelist, is found dead after his 85th "
                    "birthday celebrations. However, as detective Benoit Blanc investigates the "
                    "case, it unravels a ploy of sinister intentions."
                ),
                genre=MOVIE_GENRES.mystery,
                release_date=datetime(2019, 12, 5, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=False,
                imdb_rate=7.9,
                director=Person.objects.get(name="Rian Johnson"),
            ),
            Movie(
                title="Shutter Island",
                synopsis=(
                    "Teddy Daniels and Chuck Aule, two US marshals, are sent to an asylum on a "
                    "remote island in order to investigate the disappearance of a patient, where "
                    "Teddy uncovers a shocking truth about the place."
                ),
                genre=MOVIE_GENRES.mystery,
                release_date=datetime(2010, 3, 12, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=8.2,
                director=Person.objects.get(name="Martin Scorsese"),
            ),
            Movie(
                title="Hide and Seek",
                synopsis=(
                    "After his wife's death, David moves to Upstate New York with his daughter "
                    "Emily, who makes an imaginary friend named Charlie. But soon unexplained "
                    "events begin taking place in their house."
                ),
                genre=MOVIE_GENRES.mystery,
                release_date=datetime(2005, 1, 28, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=5.9,
                director=Person.objects.get(name="John Polson"),
            ),
            Movie(
                title="13 Going on 30",
                synopsis=(
                    "Jenna Rink makes an unusual wish on her birthday. Miraculously, her wish comes"
                    " true and the 13-year-old Jenna wakes up the next day as a 30-year-old woman."
                ),
                genre=MOVIE_GENRES.romance,
                release_date=datetime(2004, 4, 23, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=6.2,
                director=Person.objects.get(name="Gary Winick"),
            ),
            Movie(
                title="Don't Look Up",
                synopsis=(
                    "Two low-level astronomers must go on a giant media tour to warn mankind of an "
                    "approaching comet that will destroy planet Earth."
                ),
                genre=MOVIE_GENRES.comedy,
                release_date=datetime(2021, 12, 9, 3, 59, 0, 99999, tzinfo=utc),
                is_available_on_netflix=True,
                imdb_rate=7.2,
                director=Person.objects.get(name="Adam McKay"),
            ),
            Movie(
                title="Big Fish",
                synopsis=(
                    "Will Bloom returns home to care for his dying father, who had a penchant for "
                    "telling unbelievable stories. After he passes away, Will tries to find out if "
                    "his tales were really true."
                ),
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
