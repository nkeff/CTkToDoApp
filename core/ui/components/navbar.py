import customtkinter as ctk
from core.ui.components.component_sidebar_button import SidebarButton
import uuid

BASE_FG_COLOR = ("gray75", "gray25")


class Navbar(ctk.CTkFrame):
    def __init__(self,
                 master,
                 sidebar_width=170,
                 default_frame=0,
                 **kwargs):
        super().__init__(master, **kwargs)

        self.default_frame = default_frame

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=sidebar_width, corner_radius=0)
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)

        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.sidebar_frame.configure(fg_color="transparent")
        self.main_frame.configure(fg_color="yellow")

        self.buttons_list = []
        self.frames_list = []

        self._sidebar_btn_callback(default_frame)

    def add_frame(self, button_text: str, frame=None):
        btn_id = len(self.buttons_list)
        btn = SidebarButton(master=self.sidebar_frame,
                            text=button_text,
                            command=lambda: self._sidebar_btn_callback(btn_id))
        self.buttons_list.append(btn)

        if not frame:
            frame = ctk.CTkFrame(master=self, corner_radius=0, fg_color=button_text)  # todo - color delete

        self.frames_list.append(frame)

        self._render()

    def _render(self, btn_id=None):

        id = btn_id if btn_id else self.default_frame
        # draw all buttons
        for i, btn in enumerate(self.buttons_list):
            btn.grid(row=i, column=0)

        # set button color for selected button
        for i, btn in enumerate(self.buttons_list):
            if i == id:
                btn.configure(fg_color=BASE_FG_COLOR)
            else:
                btn.configure(fg_color="transparent")

        # draw_selected_frame
        for i, frame in enumerate(self.frames_list):
            if i == id:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()

    def _sidebar_btn_callback(self, btn_id):
        self._render(btn_id)


class NavbarFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.configure(corner_radius=0)
