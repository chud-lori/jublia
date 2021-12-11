import json
import pytest
from app import create_app

app = create_app()

headers = {"Content-Type": "application/json"}

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_post_email(client):
    data = {
        "event_id": "1",
        "email_subject": "Seminar about technology",
        "email_content": "Come to our seminar",
        "timestamp": "2021-12-11 15:52:00",
    }

    response = client.post("/save_emails", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert "created" in response_data['message']
    assert 1 == response_data['status']

def test_post_email_missing_input(client):
    data = {
        "email_subject": "Seminar about technology",
        "email_content": "Come to our seminar",
        "timestamp": "2021-12-11 15:52:00",
    }

    response = client.post("/save_emails", data=json.dumps(data), headers=headers)
    response_data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert "is required" in response_data['message']
    assert 0 == response_data['status']