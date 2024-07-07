from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_Jesus_Salvador():
    client = TestClient(app)  # Arrange  (organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Garantia)
    assert response.json() == {'message': 'Jesus Cristo meu Salvador'}
