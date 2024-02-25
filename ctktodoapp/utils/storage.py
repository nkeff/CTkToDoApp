import dataclasses
import os
import orjson
import uuid
from ctktodoapp.settings import Settings
from datetime import datetime


@dataclasses.dataclass
class Task(object):
    def __init__(self,
                 title: str,
                 text: str,
                 task_id=None,
                 already_done: bool = False,
                 importance_level: int = 0,
                 created_at: str = None,
                 ):
        self.title: str = title
        self.text: str = text
        self.task_id = task_id if task_id is not None else uuid.uuid4()
        self.already_done: bool = already_done
        self.importance_level: int = importance_level
        self.created_at: str = created_at if created_at is not None else datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")


def singleton(class_):
    """ декоратор для создания статического класса (SINDLTON) """
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Storage:
    """ может быть оптимизирован (храним флаг некий)"""

    def __init__(self):
        self.__data: list[Task] = []

    def add_task(self, task: Task):
        self.__data.append(task)
        self.__save()

    def update_task(self, task: Task):
        self.__load()
        for i, _task in enumerate(self.__data):
            if _task.task_id == task.task_id:
                self.__data[i] = task
        self.__save()

    def get_all_tasks(self) -> list[Task]:
        self.__load()
        return self.__data

    def __load(self):
        print("load")
        if os.path.exists(Settings.STORAGE_PATH):
            with open(Settings.STORAGE_PATH, "rb") as f:
                from_file = f.read()
                print(from_file)
                if from_file:
                    self.__data = [Task(**i) for i in orjson.loads(from_file)]

    def __save(self):
        print("save")
        tp_save = orjson.dumps(self.__data)
        with open(Settings.STORAGE_PATH, "wb") as f:
            f.write(tp_save)
