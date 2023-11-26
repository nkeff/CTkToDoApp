import customtkinter


class SidebarButton(customtkinter.CTkButton):
    
    def __init__(self, master, text, command, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            master,
            # corner_radius=8,
            # height=30,
            # width=70,
            # border_spacing=5,
            text=text,
            # fg_color="transparent",
            # text_color=("gray10", "gray90"),
            # hover_color=("gray70", "gray30"),
            anchor="center",
            command=command
        )
