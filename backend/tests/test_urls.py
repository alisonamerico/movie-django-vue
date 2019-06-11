
from backend.urls import urlpatterns

"""
Teste que valida a quantidade de urls no Root(raiz da API).

"""


def test_urls_len():
    assert 1 <= len(urlpatterns)
