from django.db import models
"""
Representação do banco de dados com seus respectivos campos referente aos filmes.
"""


class Movie(models.Model):
    movie_title = models.CharField(max_length=120)
    genres = models.CharField(max_length=120)
    duration = models.IntegerField()
    title_year = models.IntegerField()
    director_name = models.CharField(max_length=120)
    imdb_score = models.DecimalField(max_digits=2, decimal_places=1)
    picture = models.FileField()

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.movie_title  # pragma: no cover
