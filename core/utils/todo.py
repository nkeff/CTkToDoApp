from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    title: str
    text: str
    id: int = 0
    already_done: bool = False
    importance_level: int = 0
    created_at: datetime = datetime.today()


class ToDo:
    def __init__(self):
        self._task_list: list[Task] = []

    def add_task(self, task: Task):
        self._task_list.append(task)

    def get_task(self, task_index: int) -> Task | None:
        if 0 < task_index < len(self._task_list):
            return self._task_list[task_index]
        return None

    def get_all_tasks(self) -> list[Task]:
        return self._task_list
