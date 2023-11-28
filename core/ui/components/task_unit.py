import customtkinter as ctk

from core.utils.todo import Task

TASK_UNIT_PAD = 10
HIGHLIGHTED_COLOR = ("gray75", "gray25")
HIGHLIGHTED_HOVER_COLOR = ("gray70", "gray30")


class TaskUnit(ctk.CTkFrame):
    def __init__(self,
                 master,
                 task: Task,
                 **kwargs):
        super().__init__(master, **kwargs)

        self._task: Task = task

        self.grid_columnconfigure(1, weight=1)
        self.configure(corner_radius=10)

        self.id = ctk.CTkLabel(master=self, text=str(self._task.id), width=50, height=50, fg_color=HIGHLIGHTED_COLOR, corner_radius=10)
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
