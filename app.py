import os
import customtkinter

from core.ui.components.ctknavbar import CtkNavbar
from core.settings import Settings

PADDING = 20

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

        nav = CtkNavbar(master=self, default_page=0, end_buttons_count=2)
        nav.add_page(button_text="Home")
        nav.add_page(button_text="TEST")
        nav.add_page()
        nav.add_page(button_text="About")

        nav.grid(row=0, column=0, sticky="nsew")


    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)
    #     self.CONFIG.set("APPEARANCE", new_appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()
