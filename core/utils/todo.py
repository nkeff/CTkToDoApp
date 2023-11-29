import customtkinter as ctk
from dataclasses import dataclass
from datetime import datetime

TASK_UNIT_PAD = 10
HIGHLIGHTED_COLOR = ("gray75", "gray25")
HIGHLIGHTED_HOVER_COLOR = ("gray70", "gray30")
PADDING = 7


@dataclass
class Task:
    title: str
    text: str
    id: int
    already_done: bool = False
    importance_level: int = 0
    created_at: datetime = datetime.today()


class ToDo:
    def __init__(self):
        self._task_list: list[Task] = []

    def new_task(self, title: str, text: str):
        task_id = self._get_new_task_id()
        new_task = Task(id=task_id, title=title, text=text)
        self._task_list.append(new_task)

    def add_task(self, task: Task):
        self._task_list.append(task)

    def get_task(self, task_index: int) -> Task | None:
        if 0 < task_index < len(self._task_list):
            return self._task_list[task_index]
        return None

    def get_all_tasks(self) -> list[Task]:
        return self._task_list

    def pack_tasks_at_frame(self, frame, _already_done: bool = None):
        if _already_done is not None:
            task_list = [i for i in self._task_list if i.already_done == _already_done]
        else:
            task_list = self._task_list
        for i, task_unit in enumerate([TaskUnit(master=frame, task=task_i) for task_i in task_list]):
            task_unit.grid(row=i, column=0, padx=PADDING, pady=(PADDING, 0), sticky="new")

    def _get_new_task_id(self) -> int:
        return max([i.id for i in self._task_list]) + 1 if self._task_list else 0


class TaskUnit(ctk.CTkFrame):
    def __init__(self,
                 master,
                 task: Task,
                 **kwargs):
        super().__init__(master, **kwargs)

        self._task: Task = task

        self.grid_columnconfigure(1, weight=1)
        self.configure(corner_radius=10)

        self.id = ctk.CTkLabel(master=self,
                               text=str(self._task.id),
                               width=50,
                               height=50,
                               fg_color=HIGHLIGHTED_COLOR,
                               corner_radius=10)
        self.title = ctk.CTkLabel(master=self, text=self._task.title, anchor='w')
        self.text = ctk.CTkLabel(master=self, text=self._task.text, anchor='w')
        self.checkbox = ctk.CTkCheckBox(master=self,
                                        text='',
                                        width=0,
                                        height=50,
                                        checkbox_width=27,
                                        checkbox_height=27,
                                        fg_color=HIGHLIGHTED_COLOR,
                                        hover_color=HIGHLIGHTED_HOVER_COLOR,
                                        corner_radius=10)

        self.id.grid(row=0, column=0, rowspan=2, padx=TASK_UNIT_PAD, pady=TASK_UNIT_PAD, sticky="nsw")
        self.title.grid(row=0, column=1, padx=0, pady=(TASK_UNIT_PAD, 0), sticky="nsew")
        self.text.grid(row=1, column=1, padx=0, pady=(0, TASK_UNIT_PAD), sticky="nsew")
        self.checkbox.grid(row=0, column=2, rowspan=2, padx=TASK_UNIT_PAD, pady=TASK_UNIT_PAD, sticky="nse")
