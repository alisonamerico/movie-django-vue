from backend.movie.apps import MovieConfig

"""
Valida a aplicação que está sendo utilizada.
"""


def test_home():
    assert MovieConfig.name == 'movie'
