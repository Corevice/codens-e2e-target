import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json["message"] == "pong"

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_calculate_valid(client):
    response = client.get("/calculate?a=10&b=2")
    assert response.status_code == 200
    assert response.json["result"] == 5.0

def test_calculate_divide_by_zero(client):
    """division by zero should return 400 error"""
    response = client.get("/calculate?a=10&b=0")
    assert response.status_code == 400
    assert "error" in response.json

def test_calculate_default_params(client):
    response = client.get("/calculate")
    assert response.status_code == 200
    assert response.json["result"] == 10.0
