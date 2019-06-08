from rest_framework import viewsets, filters
from .serializers import MovieSerializer
from .models import Movie

from rest_framework.authentication import SessionAuthentication


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = (SessionAuthentication,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('movie_title', 'director_name', 'genres', 'imdb_score')
    ordering_fields = ('movie_title', 'director_name')
