import pytest


"""
Executa testes de validação do usuário.
"""


@pytest.fixture
def resp(client, db):
    resp = client.get('/rest-auth/login/', secure=True)
    return resp


"""
Valida status code da API, antes de ser acessada com as credencias.
"""


def test_status_code(resp):
    assert resp.status_code == 405
