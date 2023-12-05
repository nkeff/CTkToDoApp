import customtkinter

import core.utils.todo
from core.settings import Settings
from core.ui.components.ctknavbar import CtkNavbar

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

        nav = CtkNavbar(master=self, default_page=0, end_buttons_count=1, label_text="Todo App")

        todo_page = core.utils.todo.ToDoFrame(master=nav)
        self.todo_page = nav.add_page(button_text="[ To Do ]", frame=todo_page)

        done_page = core.utils.todo.ToDoFrame(master=nav)
        self.done_page = nav.add_page(button_text="[Already Done]", frame=done_page)
        self.settings_page = nav.add_page(button_text="Settings")
        nav.grid(row=0, column=0, sticky="nsew")

        todo = ToDo(frame=self.todo_page, done_frame=done_page)


    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)
    #     self.CONFIG.set("APPEARANCE", new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
