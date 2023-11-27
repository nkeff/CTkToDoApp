# ToDo
Simple customtkinter todo app

|           dark            |           light           |
|:-------------------------:|:-------------------------:|
| ![alt](screenshots/1.png) | ![alt](screenshots/2.png) |

### Example of using CtkNavbar
By default, a frame with a random color is added (helps to prototype your application). 
You can pass your own frame to CtkNavbar.

```python
import CtkNavbar
import customtkinter

app = customtkinter.CTk() 

nav = CtkNavbar(master=app, default_frame=3, end_buttons_count=1)
nav.add_page(button_text="First")
nav.add_page(button_text="Second")

custom_frame = customtkinter.CTkFrame(master=nav, fg_color="orange", corner_radius=100)
nav.add_page(button_text="Third", frame=custom_frame)

nav.grid(row=0, column=0, sticky="nsew")
```
![alt](screenshots/3.png)

### The following modules for CustomTkinter were developed in the project
- CtkNavbar
