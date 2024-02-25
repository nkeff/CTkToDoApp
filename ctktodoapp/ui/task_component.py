import customtkinter

from ctktodoapp.utils.storage import Storage, Task

TASK_UNIT_PAD = 10
HIGHLIGHTED_COLOR = ("gray75", "gray25")
HIGHLIGHTED_HOVER_COLOR = ("gray70", "gray30")
PADDING = 7


class TaskUnit(customtkinter.CTkFrame):
    def __init__(self, master, task: Task, **kwargs):
        super().__init__(master, **kwargs)

        self._task: Task = task
        self.__storage = Storage()
        self.master = master

        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1)
        self.configure(corner_radius=10)

        self.title = customtkinter.CTkLabel(
            master=self,
            text=long_text_handler(self._task.title, max_len=20),
            anchor='w',
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.text = customtkinter.CTkLabel(
            master=self,
            text=long_text_handler(self._task.text, max_len=40),
            anchor='w',
            font=customtkinter.CTkFont(size=14)
        )

        self.checkbox_var = customtkinter.StringVar(value="on" if self._task.already_done else "off")
        self.checkbox = customtkinter.CTkCheckBox(master=self,
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

        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.checkbox.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nse")

    def _checkbox_event(self):
        self._task.already_done = True if self.checkbox_var.get() == "on" else False
        self.__storage.update_task(self._task)


def long_text_handler(txt: str, max_len=30) -> str:
    res = ''
    for i, ch in enumerate(txt):
        if i % max_len == 0:
            res += '\n'
        res += ch
    return res

