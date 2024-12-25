
from app.main import *



def test_delete_task(client):
    client.post("/reset")
        # タスクを追加するリクエストを送信
    response = client.post("/tasks", json={"title": "test-delete-task", "completed": False})
    assert response.status_code == 200
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    # タスクが削除されたことを確認
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 0  # タスクリストが空であることを確認

def test_delete_non_existent_task(client):
    client.post('/reset')

    # 存在しないタスクを削除しようとする
    response = client.delete("/tasks/999")  # 存在しないID
    assert response.status_code == 404  # 削除対象がない場合は404エラー


#空のタスクリストを削除する処理のロジックはこのテストと同じため省略している
def test_delete_non_existant_task(client):
    client.post('/reset')

    response = client.delete("/tasks/111")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
