from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

import django_js_reverse.views
from common.routes import routes as common_routes
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

routes = common_routes
for route in routes:
    router.register(route["regex"], route["viewset"], basename=route["basename"])

urlpatterns = [
    path("", include("common.urls"), name="common"),
    path("admin/", admin.site.urls, name="admin"),
    path("jsreverse/", django_js_reverse.views.urls_js, name="js_reverse"),
    path("api/", include(router.urls), name="api"),
    re_path(r"^cinema/", include("cinema.urls"), name="cinema"),
]

if "silk" in settings.INSTALLED_APPS:
    urlpatterns += [re_path(r"^silk/", include("silk.urls", namespace="silk"))]
