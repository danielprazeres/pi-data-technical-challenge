from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_character():
    character_data = {
        "id": 1,
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1998
    }
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 200
    assert response.json()["name"] == character_data["name"]

def test_get_character():
    response = client.get("/character/get/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_all_characters():
    response = client.get("/character/getAll")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_character():
    response = client.delete("/character/delete/1")
    assert response.status_code == 200
    assert "message" in response.json() 