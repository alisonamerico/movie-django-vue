import pytest
from django.test import Client
from model_mommy import mommy

"""
Executa testes referentes à página inicial(home) da API - (API Root)
"""


@pytest.fixture
def home_resp(client):
    return _resp(client)


def _resp(client):
    """Função simples para evitar _pytest.warning_types.RemovedInPytest4Warning: Fixture "resp" chamado diretamente."""
    return client.get('/api/', secure=True)


@pytest.fixture
def home_resp_with_user(django_user_model, client: Client):
    user = mommy.make(django_user_model)  # pragma: no cover
    client.force_login(user)  # pragma: no cover
    return _resp(client)  # pragma: no cover


def test_home_status_code(home_resp):
    assert 200 == home_resp.status_code
