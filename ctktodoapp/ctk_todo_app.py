import customtkinter
from ctknavbar import CTkNavbar

from ctktodoapp.settings import Settings
from ctktodoapp.ui.add_task_frame import AddNewTaskFrame
from ctktodoapp.ui.setting_frame import SettingFrame
from ctktodoapp.ui.todo_frame import TodoFrame

customtkinter.set_default_color_theme("dark-blue")
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

        self.NAV = CTkNavbar(master=self, default_page=0, end_buttons_count=1, label_text="Todo App")
        self.todo_frame = TodoFrame(master=self.NAV, rf=self.render)
        self.NAV.add_page(button_text="[ To Do ]", frame=self.todo_frame)
        self.NAV.add_page(button_text="Настройки", frame=SettingFrame(master=self.NAV))
        self.NAV.grid(row=0, column=0, sticky="nsew")

    def render(self):
        self.todo_frame.render()


if __name__ == "__main__":
    app = App()
    app.mainloop()
