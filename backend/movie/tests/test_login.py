import pytest

"""
Executa testes de validação do status code usuário ao site.
"""


@pytest.fixture
def resp(client, db):
    resp = client.get('/rest-auth/login/', secure=True)
    return resp


def test_status_code(resp):
    assert resp.status_code == 405
