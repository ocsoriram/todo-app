from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks", json={"id":1,"title": "Test Task", "completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["completed"] is False

def test_create_task_missing_fields():
    # 必須フィールドが欠けたリクエスト
    response = client.post("/tasks", json={"id": 1})
    assert response.status_code == 422  # FastAPIはバリデーションエラーで422を返す

def test_create_task_invalid_field_types():
    # "id" を文字列にする
    response = client.post("/tasks", json={"id": "one", "title": "Invalid Task", "completed": "no"})
    assert response.status_code == 422  # 型エラー
    assert "detail" in response.json()  # エラーメッセージを確認

def test_create_task_duplicate_id():
    # タスクを1つ追加
    tasks.append(Task(id=1, title="Existing Task", completed=False))
    
    # 同じIDを使って新しいタスクを作成
    response = client.post("/tasks", json={"id": 1, "title": "Duplicate Task", "completed": False})
    assert response.status_code == 400  # ID重複エラー
    assert response.json()["detail"] == "Task ID already exists"

def test_create_task_empty_request():
    response = client.post("/tasks", json={})
    assert response.status_code == 422  # バリデーションエラー
    assert "detail" in response.json()

  
