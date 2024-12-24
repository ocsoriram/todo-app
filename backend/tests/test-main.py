from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Test Task", "completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["completed"] is False