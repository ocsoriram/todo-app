import pytest
from app.main import tasks

@pytest.fixture(autouse=True)
def clear_tasks():
    tasks.clear()  # 各テスト前にタスクをリセット