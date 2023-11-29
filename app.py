import customtkinter

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
        self.todo_page = nav.add_page(button_text="[ To Do ]")
        self.done_page = nav.add_page(button_text="[Already Done]")
        self.settings_page = nav.add_page(button_text="Settings")
        nav.grid(row=0, column=0, sticky="nsew")

        todo = ToDo()
        todo.new_task(title="Task 1", text="lskjdfalskdhfsadfsakjdflkjsadhflkhsadfkjhsadf")
        todo.new_task(title="Task 2", text="lskjdfalskdhfsadfsakjdflkjsadhflkhsadfkjhsadf")
        todo.new_task(title="Task 3", text="lskjdfalskdhfsadfsakjdflkjsadhflkhsadfkjhsadf")
        todo.new_task(title="Task 4", text="lskjdfalskdhfsadfsakjdflkjsadhflkhsadfkjhsadf")
        todo.new_task(title="Task 5", text="lskjdfalskdhfsadfsakjdflkjsadhflkhsadfkjhsadf")
        todo.new_task(title="Task 6", text="lskjdfalskdhfsadfsakjdflkjsadhflkhsadfkjhsadf")

        todo.pack_tasks_at_frame(frame=self.todo_page, _already_done=False)

    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)
    #     self.CONFIG.set("APPEARANCE", new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
