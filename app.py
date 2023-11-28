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

        nav = CtkNavbar(master=self, default_page=2, end_buttons_count=2)
        nav.add_page(button_text="Home")
        nav.add_page()
        nav.add_page()
        nav.add_page(button_text="About")

        a = customtkinter.CTkButton(master=nav.sidebar_frame, text="SETTINGS", fg_color=("red", "green"))
        nav.add_page(button_text="Settings", btn=a)

        nav.grid(row=0, column=0, sticky="nsew")

        a = customtkinter.CTkButton(master=self, command=lambda: nav.add_page(button_text="NEW BUTTON"))
        a.grid(row=1, column=0, sticky="nsew")


        # nav.render()


        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        #
        # # == sidebar frame == #
        # self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        # self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        # self.sidebar_frame.configure(fg_color="transparent")
        # # self.sidebar_frame.grid_rowconfigure(5, weight=1)
        #
        # # == main frame == #
        # self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        # self.main_frame.grid(row=0, column=1, sticky="nsew")
        #
        # sidebar_buttons = [
        #     (
        #         SidebarButton(master=self.sidebar_frame, text="qwe", command=lambda: self.test_func(0)),
        #         SidebarBaseFrame(master=self.main_frame)
        #     ),
        #     (
        #         SidebarButton(master=self.sidebar_frame, text="asd", command=lambda: self.test_func(1)),
        #         SidebarBaseFrame(master=self.main_frame)
        #     ),
        #     (
        #         SidebarButton(master=self.sidebar_frame, text="zxc", command=lambda: self.test_func(2)),
        #         SidebarBaseFrame(master=self.main_frame)
        #     )
        # ]
        #
        # for i, btn in enumerate(sidebar_buttons):
        #     btn[0].grid(row=i, column=0)

        # ================ SIDEBAR Кнопки ================ #
        # self.sidebar_button_1 = SidebarButton(self.sidebar_frame, frame=self.FRAME_1,
        #                                       command=self.sidebar_button_1_event)
        # self.sidebar_button_1.grid(row=1, column=0, sticky="ew")

        # ================ FRAME 1 ПОМОГАТОР ================ #
        # self.frame_1 = core.ui.frames.FrameHelper(master=self)
        # self.frame_1.grid_columnconfigure(0, weight=1)

        # # ВЫБЕРЕМ ДЕФОЛТНЫЙ ФРЕЙМ (ЕСЛИ НАСТРОЙКИ НЕ ЗАПОЛНЕНЫ - ТО НАСТРОЙКИ)
        # if self.CONFIG.get("LIBREOFFICE_PATH") == '':
        #     self.select_frame_by_name(self.FRAME_4)
        # else:
        #     self.select_frame_by_name(self.FRAME_1)


    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)
    #     self.CONFIG.set("APPEARANCE", new_appearance_mode)

    def test_func(self, param):
        print(param)


if __name__ == "__main__":
    app = App()
    app.mainloop()
