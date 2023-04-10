from customtkinter import *
import json
import sys
sys.path.append("./")
with open("resources/f_keys.json", "r", encoding="utf-8") as f:
    f_keys=json.load(f)
       
# Main prefs
set_appearance_mode("system")
set_default_color_theme("green")

class Window(CTk):
    def __init__(self, width, height) -> None:
        super().__init__()


        # shirina
        self.width = width

        # visota
        self.height = height

        # App title and geometry
        self.title("Custom Keybinds")
        self.geometry(f"{self.width}x{self.height}")

        # App grid
        self.grid_columnconfigure((1,2,3,4,5), weight=1)
        self.grid_rowconfigure((1,2,3,4,5), weight=1)

        def create_dropdowns(self):
            for i in range(10):
                droplabel = CTkLabel(self, text=f"F {i+1}: ")
                
                dropdown = CTkComboBox(self, values=list(self.f_keys.json()))
                if i < 5:
                    droplabel.grid(row=i+1, column=0, padx=10, pady=10)
                    dropdown.grid(row=i+1, column=1, padx=10, pady=10)
                elif i >= 5:
                    droplabel.grid(row=i-4, column=3, padx=10, pady=10)
                    dropdown.grid(row=i-4, column=4, padx=10, pady=10)
                self.dropdowns.append(dropdown)

if __name__ == "__main__":   
    root = CTk()
    app = Window(1280, 720)
    app.mainloop()