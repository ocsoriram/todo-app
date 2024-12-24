from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)

def test_update_task():
    # テストの準備：タスクリストをクリアして新しいタスクを作成
    tasks.clear()  # グローバル変数をリセット

    # タスクを追加するリクエストを送信
    response = client.post("/tasks", json={"id": 1, "title": "test-update-task", "completed": False})
    assert response.status_code == 200

    # タスクを更新するリクエストを送信
    response = client.put("/tasks/1", json={"id": 1, "title": "Updated Task", "completed": True})
    assert response.status_code == 200

    # 更新されたタスクの内容を確認
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Updated Task"
    assert data["completed"] is True