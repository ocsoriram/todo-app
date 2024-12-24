from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []
