from django.shortcuts import render

from cinema.models import Movie


def movies_list(request):
    template_name = "movies/movies_list.html"
    context = {
        "movies": Movie.objects.select_related("director").prefetch_related("cast").all(),
    }

    return render(request, template_name, context)
