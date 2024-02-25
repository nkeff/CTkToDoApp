import customtkinter
from ctkgridlayout import CTkGridLayout


class SettingFrame(customtkinter.CTkFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid_frame = CTkGridLayout(master=self, column_count=2, padding=100, spacing=15, fg_color="transparent")
        self.grid_frame.add_items([
            customtkinter.CTkLabel(
                master=self.grid_frame,
                text="Изменить тему приложения"
            ),
            customtkinter.CTkSwitch(
                master=self.grid_frame,
                text="",
                command=lambda: customtkinter.set_appearance_mode(
                    "Dark" if customtkinter.get_appearance_mode() == "Light" else "Light")
            ),

            customtkinter.CTkLabel(
                master=self.grid_frame,
                text="Изменить масштабирование"
            ),
            customtkinter.CTkOptionMenu(
                master=self.grid_frame,
                width=100,
                height=50,
                values=["100%", "80%", "90%", "110%", "120%"],
                command=lambda x: customtkinter.set_widget_scaling(int(x.replace("%", "")) / 100)
            ),

        ])

        self.grid_frame.grid(row=0, column=0, sticky="nsew")

