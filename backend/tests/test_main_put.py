from app.main import *


def test_update_task(client):
    # テストの準備：タスクリストをクリアして新しいタスクを作成
    client.post("/reset")

    # タスクを追加するリクエストを送信
    response = client.post("/tasks", json={"title": "test-update-task", "completed": False})
    assert response.status_code == 200
    task_id = response.json()["id"]

    # タスクを更新するリクエストを送信
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "completed": True})
    assert response.status_code == 200

    # 更新されたタスクの内容を確認
    data = response.json()
    #assert data["id"] == 
    assert data["title"] == "Updated Task"
    assert data["completed"] is True