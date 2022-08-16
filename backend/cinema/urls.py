from django.urls import re_path

from cinema.views import movies_list


app_name = "music"

urlpatterns = [
    re_path(r"^movies/list/", movies_list, name="movies"),
]
