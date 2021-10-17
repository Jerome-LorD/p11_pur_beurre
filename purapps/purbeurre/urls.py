"""Urls app module."""
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("results/<str:product_name>/", views.results, name="results"),
    path("product/<str:product_name>/", views.product_details, name="product"),
    path("favorites/", views.favorites, name="favorites"),
    path("mentions/", views.mentions, name="mentions"),
    re_path(r"^autocomplete/", views.autocomplete, name="autocomplete"),
    path("ajax_save/", views.save_substitute, name="save_substitute"),
    path("ajax_del/", views.delete_substitute, name="delete_substitute"),
    path("ajax_get/", views.get_reference_id, name="get_reference_id"),
]
