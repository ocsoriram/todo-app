

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

#Taskモデル
class Task(BaseModel):
    id: int
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
    new_task = Task(id=len(tasks) + 1, title=task.title, completed=task.completed)
    tasks.append(new_task)
    return new_task

#タスクを更新する
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, update_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = update_task
            return update_task
    raise HTTPException(status_code=404, detail="Task not found")

# タスクを削除
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted successfully"}
