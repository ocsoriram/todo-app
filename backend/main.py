from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORSの設定（Reactからアクセスを許可するため）
origins = [
    "http://localhost:3000",  # Reactのアプリが動く場所
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 仮のTodoリスト
todos = []

@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(item: dict):
    todos.append(item)
    return {"message": "OK"}