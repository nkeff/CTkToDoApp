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


class ToDoFrame(ctk.CTkFrame):
    def __init__(self,
                 master,
                 **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.todopage = ctk.CTkScrollableFrame(master=self, fg_color="gray12")

        self.todopage.grid_columnconfigure(0, weight=1)
        self.todopage.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.title_input = ctk.CTkEntry(master=self)
        self.text_input = ctk.CTkEntry(master=self)
        self.add_button = ctk.CTkButton(master=self)

        self.title_input.grid(row=1, column=0, sticky="nsew")
        self.text_input.grid(row=1, column=1, sticky="nsew")
        self.add_button.grid(row=2, column=0, columnspan=2, sticky="nsew")


class ToDo:
    def __init__(self, frame):
        self._task_list: list[Task] = []
        self._already_done_task_list: list[Task] = []
        self._frame = frame

    def new_task(self, title: str, text: str):
        new_task = Task(id=self._get_new_task_id(), title=title, text=text)
        self._task_list.append(new_task)

    def add_task(self, task: Task):
        self._task_list.append(task)

    def get_task_index(self, task: Task) -> int | None:
        for i, task_i in enumerate(self._task_list):
            if task_i.id == task.id:
                return i
        return None

    def get_all_tasks(self) -> list[Task]:
        return self._task_list

    def update_task(self, _task: Task):
        index = None
        for i, task in self._task_list:
            if _task.id == task.id:
                index = i

        if index is not None:
            self._task_list.insert(index, _task)

    def _render(self):
        """
        todo - create a common render function
        :return:
        """
        pass

    def pack_tasks_at_frame(self, _already_done: bool = None):
        if _already_done is not None:
            task_list: list[Task] = [i for i in self._task_list if i.already_done == _already_done]
        else:
            task_list: list[Task] = self._task_list
        task_list = sorted(task_list, key=lambda x: x.already_done)
        for i, task_unit in enumerate(
                [TaskUnit(master=self._frame.todopage,
                          task=task_i,
                          _checkbox_callback=self._checkbox_callback)
                 for task_i in task_list]):
            task_unit.grid(row=i, column=0, padx=PADDING, pady=(PADDING, 0), sticky="new")

    def _get_new_task_id(self) -> int:
        return max([i.id for i in self._task_list]) + 1 if self._task_list else 0

    def _checkbox_callback(self, task: Task):
        self._task_list[self.get_task_index(task)] = task
        self.pack_tasks_at_frame()


class TaskUnit(ctk.CTkFrame):
    def __init__(self,
                 master,
                 task: Task,
                 _checkbox_callback,
                 **kwargs):
        super().__init__(master, **kwargs)

        self._task: Task = task
        self._checkbox_callback = _checkbox_callback

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

        self.checkbox_var = ctk.StringVar(value="on" if self._task.already_done else "off")
        self.checkbox = ctk.CTkCheckBox(master=self,
                                        text='',
                                        variable=self.checkbox_var,
                                        onvalue="on", offvalue="off",
                                        command=self._checkbox_event,
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

    def _checkbox_event(self):
        self._task.already_done = True if self.checkbox_var.get() == "on" else False
        self._checkbox_callback(task=self._task)
        # print(self.checkbox_var.get(), self._task.id)
