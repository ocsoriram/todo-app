

from typing import List, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

#Taskモデル
class Task(BaseModel):
    id: Optional[str] = None
    title: str
    completed: bool = False

#仮のデータストア
tasks: List[Task] = []

#全てのタスクを取得する
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

# 新しいタスクを作成する
    # @app.post("/tasks", response_model=Task)
    # def create_task(task: Task):
    #     tasks.append(task)
    #     return task

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    # 自動的にIDを割り当てる
    new_task = Task(id=str(uuid4()), title=task.title, completed=task.completed)
     # 既存のIDの重複をチェック
    if any(t.id == new_task.id for t in tasks):  
        raise HTTPException(status_code=400, detail="Task ID already exists")
    tasks.append(new_task)
    return new_task

#タスクを更新する
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, update_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = update_task
            return update_task
    raise HTTPException(status_code=404, detail="Task not found")

# タスクを削除
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    global tasks
    #削除対象のタスクが存在するか確かめるささ
    task_to_delete = next((task for task in tasks if task.id == task_id), None)
    if task_to_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    #tasksのサイズは大きくならないことが予想されるので全走査で実装
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted successfully"}


#riset用エンドポイント

@app.post("/reset")
def reset_tasks():
    tasks.clear()
    return {"status": "reset"}