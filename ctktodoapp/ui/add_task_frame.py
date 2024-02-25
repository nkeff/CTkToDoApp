import customtkinter
from ctktodoapp.utils.storage import Storage, Task

from ctkgridlayout import CTkGridLayout


class AddNewTaskFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.master = master
        self.__storage = Storage()

        self.grid_frame = CTkGridLayout(master=self, column_count=1, padding=10, spacing=5)

        self.title_input = customtkinter.CTkEntry(
            master=self.grid_frame,
            placeholder_text="Заголовок",
            height=40,
            width=300)
        self.text_input = customtkinter.CTkEntry(
            master=self.grid_frame,
            placeholder_text="Описание",
            height=40)
        self.add_button = customtkinter.CTkButton(
            master=self.grid_frame,
            text="Добавить задачу",
            height=40,
            corner_radius=10,
            command=self.add_new_task_callback)

        self.grid_frame.add_items([
            self.title_input,
            self.text_input,
            self.add_button
        ])

        self.grid_frame.grid(row=1, column=0, sticky="nsew")

    def add_new_task_callback(self):
        title = self.title_input.get()
        text = self.text_input.get()
        if title and text:
            self.__storage.add_task(Task(title=title, text=text))
            self.text_input.delete(0, len(text))
            self.title_input.delete(0, len(title))
            self.render()

    def render(self):
        self.master.render()
