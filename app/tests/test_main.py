from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200, response.json()
    assert response.json() == {"Status": "OK"}


def test_random_joke():
    response = client.post("/random_joke", headers={"x-api-key": "expected_api_key"})
    assert response.status_code == 200, response.json()
    assert "joke" in response.json()

    response = client.post(
        "/random_joke",
        headers={"x-api-key": "invalid_api_key"},
        json={"category": "dev"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}


def test_random_joke_categorized():
    response = client.post(
        "/random_joke",
        headers={"x-api-key": "expected_api_key"},
        json={"category": "dev"},
    )
    assert response.status_code == 200
    assert "joke" in response.json()


def test_joke_categories():
    response = client.get("/joke_categories", headers={"x-api-key": "expected_api_key"})
    assert response.status_code == 200
    assert "categories" in response.json()

    response = client.get("/joke_categories", headers={"x-api-key": "invalid_api_key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid API Key"}
