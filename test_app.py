import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_register(client):
    response = client.post('/request', json={"name": "sonu", "password": "abc123"})
    assert response.status_code == 200
    assert response.json == {"name": "sonu", "password": "abc123"}


def test_login(client):
    response = client.post('/login', json={"name": "sonu", "password":"abc123"})
    assert response.status_code == 200
    assert isinstance(response.json, int)


def test_borrow(client):
    response = client.post('/borrow', json={"id": 1, "book": "The Great Gatsby"})
    assert response.status_code == 200
    assert response.json == "Borrowed successfully"


def test_return_book(client):
    response = client.post('/return_book', json={"id": 1, "book": "The Great Gatsby"})
    assert response.status_code == 200
    assert response.json == "Returned successfully"


def test_search_book(client):
    response = client.post('/search_book', json={"book_name":"","id":"","author":"","title": "Gatsby"})
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert "The Great Gatsby" in response.json
