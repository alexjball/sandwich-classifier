import os

import pytest
from endpoint import app

HOT_DOG_URL='https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Hotdog_-_Evan_Swigart.jpg/320px-Hotdog_-_Evan_Swigart.jpg'
TACO_URL='https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg/320px-001_Tacos_de_carnitas%2C_carne_asada_y_al_pastor.jpg'

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_empty_request(client):
  rv = client.post('/classify')
  assert rv.status_code != 200

def test_invalid_url(client):
  rv = client.post('/classify', data={ 'url': 'https://this-is-not-a-domain.xyz' })
  assert rv.status_code != 200

def test_hot_dog_url(client):
  rv = client.post('/classify', data={ 'url': HOT_DOG_URL })
  assert rv.get_json()['class'] == 'hot_dogs'

def test_taco_url(client):
  rv = client.post('/classify', data={ 'url': TACO_URL })
  assert rv.get_json()['class'] == 'tacos'