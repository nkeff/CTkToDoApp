import os
import json
from core.settings import Settings
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Task(object):
    title: str
    text: str
    id: int
    already_done: bool = False
    importance_level: int = 0
    created_at: str = datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")


class Storage:
    storage_path = Settings.STORAGE_PATH

    @staticmethod
    def load() -> list[Task]:
        print("load")
        if os.path.exists(Storage.storage_path):
            with open(Storage.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                res = [Task(**i) for i in data]
                return res
        else:
            return []

    @staticmethod
    def save(data: list[Task]):
        print("save")
        saved_data = [asdict(i) for i in data]
        with open(Storage.storage_path, 'w', encoding='utf-8') as f:
            json.dump(saved_data, f)
