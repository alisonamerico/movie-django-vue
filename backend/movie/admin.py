from django.contrib import admin
from .models import Movie

"""
Foi utilizado no admin do django, campos como 'search', 'list' e 'filter' para facilitar a visualização dos dados.
"""


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'genres', 'director_name', 'imdb_score', 'created', 'modified']
    search_fields = ['movie_title', 'genres', 'director_name', 'imdb_score']
    list_filter = ['created', 'modified']


admin.site.register(Movie, MovieAdmin)
