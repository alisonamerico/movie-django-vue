from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer
from .models import Movie

"""
Foi usado na API um campo 'search' para pesquisar e ordenar os campos mesma.
Com autenticação via token para gerenciar o acesso dos usuários.

"""


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('movie_title', 'director_name', 'genres', 'imdb_score')
    ordering_fields = ('movie_title', 'director_name')
