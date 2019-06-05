from backend.movie.apps import MovieConfig


def test_home():
    assert MovieConfig.name == 'movie'
