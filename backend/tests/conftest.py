import pytest
from fastapi.testclient import TestClient
from app.main import app

# テストクライアントをフィクスチャとして提供
@pytest.fixture
def client():
    test_client = TestClient(app)
    
    # テスト実行前にリセット
    test_client.post("/reset")
    
    return test_client