import customtkinter
from ctkgridlayout import CTkGridLayout, CTkScrollableGridLayout

from ctktodoapp.ui.add_task_frame import AddNewTaskFrame
from ctktodoapp.ui.task_component import TaskUnit
from ctktodoapp.utils.storage import Storage, Task


class TodoFrame(customtkinter.CTkFrame):
    def __init__(self, rf, **kwargs):
        super().__init__(**kwargs)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.rf = rf
        self.__storage = Storage()
        self.__tasks: list[Task] = []
        self.grid_frame = None

        self.change_layout = customtkinter.CTkOptionMenu(
                master=self,
                height=25,
                values=['1', '2', '3'],
                command=lambda x: self.grid_frame.update_layout(column_count=int(x))
        )

        self.grid_config = {
            "column_count": 1,
            "padding": 5,
            "spacing": 5,
            "fg_color": "transparent",
        }

        self.change_layout.grid(row=0, column=0, padx=10, pady=10, sticky="nse")
        self.add_task_frame = AddNewTaskFrame(master=self)
        self.add_task_frame.grid(row=2, column=0, sticky="nsew")

        self.render()

    def render(self):
        self.__tasks: list[Task] = self.__storage.get_all_tasks()
        if self.grid_frame is not None:
            self.grid_frame.grid_forget()
        self.grid_frame = CTkScrollableGridLayout(master=self, **self.grid_config)
        self.grid_frame.add_items([TaskUnit(master=self.grid_frame, task=task) for task in self.__tasks])
        self.grid_frame.grid(row=1, column=0, sticky="nsew")
