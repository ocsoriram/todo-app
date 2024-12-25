from fastapi.testclient import TestClient
from app.main import *

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_get_tasks_with_data():
    # テスト環境を準備
    client.post("/reset")
    
    task1 = client.post("/tasks", json={"title": "Task 1", "completed": False}).json()
    task2 = client.post("/tasks", json={"title": "Task 2", "completed": True}).json()

    # タスク一覧を取得
    response = client.get("/tasks")
    assert response.status_code == 200

    #レスポンスを取得
    response_data = response.json()

    #1 順序を指定しない比較
    assert set((task["id"], task["title"], task["completed"]) for task in response_data) == set([
        (task1.get("id"), task1.get("title"), task1.get("completed")),
        (task2.get("id"), task2.get("title"), task2.get("completed"))
    ])

    #2 各タスクがレスポンスに含まれているか確認
    assert any(task["id"] == task1["id"] and task["title"] == "Task 1" and not task["completed"] for task in response_data)
    assert any(task["id"] == task2["id"] and task["title"] == "Task 2" and task["completed"] for task in response_data)

#TODO idの修正
def test_get_tasks_with_many_items():
    # 100件のタスクを追加
    for i in range(1, 101):
        client.post("/tasks", json={"title": f"Task {i}", "completed": False})
    assert response.status_code == 200

    # タスクリストを取得
    response = client.get("/tasks")
    assert response.status_code == 200

    # データサイズと内容を確認
    response_data = response.json()
    assert len(response_data) == 100

    # すべてのタスクを確認
    for i in range(1, 101):
        task_title = f"Task {i}"
        assert any(task["title"] == task_title and not task["completed"] for task in response_data)

    # task1 = response_data[0]
    # task100 = response_data[99]

    # #各タスクがレスポンスに含まれているか確認
    # assert any(task["id"] == task1["id"] and task["title"] == "Task 1" and not task["completed"] for task in response_data)
    # assert any(task["id"] == task100["id"] and task["title"] == "Task 100" and not task["completed"] for task in response_data)


#TODO idの修正
def test_get_tasks_with_invalid_query():
    client.post("/reset")
    # タスクを追加
    collect_response = client.post("/tasks", json={"title": "Task 1", "completed": False})
    assert collect_response.status_code == 200

    task = collect_response.json()
    task_id = task["id"]

    # 不正なクエリパラメータ付きでリクエスト
    response = client.get("/tasks?invalid_param=true")
    assert response.status_code == 200  # クエリパラメータは無視される
    response_data = response.json()
    assert response_data == [{"id": task_id, "title": "Task 1", "completed": False}]