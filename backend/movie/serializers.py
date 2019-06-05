from rest_framework import serializers  # pragma: no cover
from .models import Movie  # pragma: no cover


class MovieSerializer(serializers.ModelSerializer):  # pragma: no cover

    class Meta:  # pragma: no cover
        model = Movie  # pragma: no cover
        fields = (  # pragma: no cover
            "id", "movie_title", "genres", "duration",   # pragma: no cover
            "title_year", "director_name", "imdb_score", "picture"  # pragma: no cover
        )  # pragma: no cover
