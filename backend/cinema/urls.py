from django.urls import re_path

from cinema.views import ArtistsListView, AwardsListView, MoviesListView


app_name = "music"

urlpatterns = [
    re_path(r"^movies/list/", MoviesListView.as_view(), name="movies"),
    re_path(r"^artists/list/", ArtistsListView.as_view(), name="artists"),
    re_path(r"^awards/list/", AwardsListView.as_view(), name="awards"),
]
