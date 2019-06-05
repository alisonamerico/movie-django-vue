import pytest

from django_assertions import dj_assert_contains

"""
Executa testes de validação do usuário.
"""


@pytest.fixture
def resp(client, db):
    resp = client.get('/api-auth/login/?next=/', secure=True)
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'content',
    [
        '<form',
        '<input type="text" name="username"',
        '<input type="password" name="password"',
        'type="submit"',
    ]
)
def test_page_content(content, resp):
    dj_assert_contains(resp, content)
