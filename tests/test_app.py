import pytest
from src.app.app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Student Engagement API is running." in response.data

def test_predict(client):
    data = {'feedback_text': 'The student engagement is low and needs improvement.'}
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['status'] == 'success'
    assert response_json['sentiment'] in ['POSITIVE', 'NEGATIVE']