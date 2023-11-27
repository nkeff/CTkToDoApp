import customtkinter as ctk
import random

BASE_FG_COLOR = ("gray75", "gray25")


class CtkNavbar(ctk.CTkFrame):
    def __init__(self,
                 master,
                 sidebar_width=170,
                 auto_render=True,
                 default_frame=0,
                 **kwargs):
        super().__init__(master, **kwargs)

        self._default_frame = default_frame
        self._auto_render = auto_render

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)

        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        self.buttons_list = []
        self.frames_list = []

    def add_frame(self, button_text: str, frame=None):
        btn_id = len(self.buttons_list)
        btn = DefaultSidebarButton(master=self.sidebar_frame,
                                   text=button_text,
                                   command=lambda: self._render(btn_id))
        self.buttons_list.append(btn)

        if not frame:
            frame = DefaultNavbarFrame(master=self)

        self.frames_list.append(frame)

        if self._auto_render:
            self._render()

    def grid(self, **kwargs):
        """
        Render everything at the moment when the navigation block is added to the program
        """
        super().grid(**kwargs)
        if self._auto_render:
            self._render(btn_id=self._default_frame)

    def render(self):
        """
        Render manually
        """
        self._render()

    def _render(self, btn_id=None):
        """
        Render all blocks
        """
        _default_frame = self._default_frame if self._default_frame in range(len(self.buttons_list)) else 0
        chosen_frame_id = btn_id if btn_id else _default_frame

        # draw all buttons
        for i, btn in enumerate(self.buttons_list):
            btn.grid(row=i, column=0, padx=6, pady=3)

        # set button color for selected button
        for i, btn in enumerate(self.buttons_list):
            if i == chosen_frame_id:
                btn.configure(fg_color=BASE_FG_COLOR)
            else:
                btn.configure(fg_color="transparent")

        # draw_selected_frame
        for i, frame in enumerate(self.frames_list):
            if i == chosen_frame_id:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()


class DefaultSidebarButton(ctk.CTkButton):
    """
    Default sidebar button
    If you want to use custom sidebar button, you can do it)
    """

    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            master,
            corner_radius=8,
            height=40,
            border_spacing=5,
            text=text,
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="center",
            command=command
        )


class DefaultNavbarFrame(ctk.CTkFrame):
    """
    Default sidebar frame
    It's created with corner_radius=0 and random background color
    (Use for prototype your app)
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.configure(corner_radius=0, fg_color=self._get_random_color())

    @staticmethod
    def _get_random_color() -> str:
        return f"#{''.join([random.choice("123456789ABCDEF") for i in range(6)])}"
