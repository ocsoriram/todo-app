from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_get_tasks_with_data():
    # テスト環境を準備
    tasks.clear()
    
    client.post("/tasks", json={"id": 1, "title": "Task 1", "completed": False})
    client.post("/tasks", json={"id": 2, "title": "Task 2", "completed": True})

    # タスク一覧を取得
    # リクエストを送信
    response = client.get("/tasks")
    assert response.status_code == 200

    # タスクリストが正しい内容を返すか確認
    assert response.json() == [
        {"id": 1, "title": "Task 1", "completed": False},
        {"id": 2, "title": "Task 2", "completed": True},
    ]

def test_get_tasks_with_many_items():
    # 100件のタスクを追加
    for i in range(1, 101):
        client.post("/tasks", json={"id": i, "title": f"Task {i}", "completed": False})

    # タスクリストを取得
    response = client.get("/tasks")
    assert response.status_code == 200

    # データサイズと内容を確認
    data = response.json()
    assert len(data) == 100
    assert data[0] == {"id": 1, "title": "Task 1", "completed": False}
    assert data[-1] == {"id": 100, "title": "Task 100", "completed": False}

def test_get_tasks_with_invalid_query():
    client.post("/reset")
    # タスクを追加
    client.post("/tasks", json={"id": 1, "title": "Task 1", "completed": False})

    # 不正なクエリパラメータ付きでリクエスト
    response = client.get("/tasks?invalid_param=true")
    assert response.status_code == 200  # クエリパラメータは無視される
    assert response.json() == [{"id": 1, "title": "Task 1", "completed": False}]