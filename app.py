import customtkinter

from core.settings import Settings
from core.ui.components.ctknavbar import CtkNavbar
from core.ui.components.task_unit import TaskUnit

from core.utils.todo import Task, ToDo

PADDING = 7

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("System")
customtkinter.set_widget_scaling(1)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title(Settings.APP_NAME)
        self.geometry(Settings.GEOMETRY)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        nav = CtkNavbar(master=self, default_page=0, end_buttons_count=1)
        self.todo_page = nav.add_page(button_text="[ To Do ]")
        self.done_page = nav.add_page(button_text="[Already Done]")
        self.settings_page = nav.add_page(button_text="Settings")
        nav.grid(row=0, column=0, sticky="nsew")

        t1 = Task(title="First task", text="some description about first task")
        t2 = Task(title="Second task", text="some description about second task")

        task1 = TaskUnit(self.todo_page, task=t1)
        task2 = TaskUnit(self.todo_page, task=t2)

        task1.grid(row=0, column=0, padx=PADDING, pady=(PADDING, 0), sticky="new")
        task2.grid(row=1, column=0, padx=PADDING, pady=(PADDING, 0), sticky="new")

    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)
    #     self.CONFIG.set("APPEARANCE", new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
