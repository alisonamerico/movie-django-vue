from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movie

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
