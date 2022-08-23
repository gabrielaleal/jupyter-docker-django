from django.views.generic import ListView
from django.db.models import Count, Q, Subquery, OuterRef

from cinema.models import Award, Movie, Person


# def movies_list(request):
#     template_name = "movies/movies_list.html"
#     context = {
#         "movies": Movie.objects.select_related("director").prefetch_related("cast").all(),
#     }

#     return render(request, template_name, context)


class MoviesListView(ListView):
    model = Movie
    queryset = Movie.objects.select_related("director").prefetch_related("cast").all()
    template_name = "movies/movies_list.html"


class ArtistsListView(ListView):
    model = Person
    paginate_by = 5
    queryset = Person.objects.annotate(
        total_awards_won=Count("nominations", filter=Q(nominations__is_winner=True))
    ).order_by("-total_awards_won")
    template_name = "artists/artists_list.html"


class AwardsListView(ListView):
    model = Award
    queryset = Award.objects.annotate(
        most_nominated_movie_title=Subquery(
            Movie.objects.annotate(
                nominations_count=Count(
                    "nominations", filter=Q(nominations__award_id=OuterRef("id"))
                )
            )
            .order_by("-nominations_count")
            .values("title")[:1]
        )
    )

    template_name = "awards/awards_list.html"


<QuerySet [<Movie: Inglourious Basterds>, <Movie: Once Upon a Time in... Hollywood>]>