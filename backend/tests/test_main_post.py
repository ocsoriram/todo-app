from app.main import *


def test_create_task(client):
    client.post("/reset")
    response = client.post("/tasks", json={"title": "Test Task", "completed": False})
    assert response.status_code == 200
    data=response.json()
    assert data["title"] == "Test Task"
    assert data["completed"] is False
    assert "id" in data
    assert isinstance(data["id"],str)

def test_create_task_missing_fields(client):
    client.post("/reset")
    # 必須フィールドが欠けたリクエスト
    response = client.post("/tasks", json={"completed": True})
    assert response.status_code == 422  # FastAPIはバリデーションエラーで422を返す

def test_create_task_invalid_field_types(client):
    client.post("/reset")
    # "id" を文字列にする
    response = client.post("/tasks", json={"id": 1, "title": "Invalid Task", "completed": "no"})
    assert response.status_code == 422  # 型エラー
    assert "detail" in response.json()  # エラーメッセージを確認

def test_create_task_duplicate_id(client):
    client.post("/reset")
    # タスクを1つ追加
    response = client.post("/tasks", json={"title": "Existing Task", "completed": False})
    assert response.status_code == 200
    data = response.json()
    
    # 同じIDを使って新しいタスクを作成
    response = client.post("/tasks", json={ "title": "Duplicate Task", "completed": False})
    assert response.status_code == 200  # 自動生成されたuuidにより重複は発生しない
    assert data["title"] == "Existing Task"

def test_create_task_empty_request(client):
    client.post("/reset")
    response = client.post("/tasks", json={})
    assert response.status_code == 422  # バリデーションエラー
    assert "detail" in response.json()

  
