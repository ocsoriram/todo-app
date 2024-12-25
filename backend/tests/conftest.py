import pytest
from fastapi.testclient import TestClient
from app.main import app

# テストクライアントをフィクスチャとして提供


@pytest.fixture(scope="session")
def client() -> TestClient:
    test_client = TestClient(app)
    
    # テスト実行前にリセット
    response = test_client.post("/reset")
    assert response.status_code == 200, "Reset endpoint failed!  Status: {response.status_code}, Body: {response.text}"
    
    return test_client