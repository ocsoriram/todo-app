from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)

def test_delete_task():
    tasks.clear()
        # タスクを追加するリクエストを送信
    response = client.post("/tasks", json={"id": 1, "title": "test-delete-task", "completed": False})
    assert response.status_code == 200

    response = client.delete("/tasks/1")
    assert response.status_code == 200

    # タスクが削除されたことを確認
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 0  # タスクリストが空であることを確認

def test_delete_non_existent_task():
    tasks.clear()

    # 存在しないタスクを削除しようとする
    response = client.delete("/tasks/999")  # 存在しないID
    assert response.status_code == 404  # 削除対象がない場合は404エラー