import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_get_item(client):
    response = client.get('/items/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Item One'

def test_get_item_not_found(client):
    response = client.get('/items/999')
    assert response.status_code == 404
    assert response.json['error'] == 'Item not found'

def test_create_item(client):
    new_item = {"name": "Item Three"}
    response = client.post('/items', json=new_item)
    assert response.status_code == 201
    assert response.json['name'] == 'Item Three'
    assert response.json['id'] == 3
