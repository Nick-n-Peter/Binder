from customtkinter import *
import json

# Appending root folder
import sys
sys.path.append('./')


with open("resources/f_keys.json", "r", encoding="utf-8") as f:
    f_keys = json.load(f)
with open("resources/keybinds.json", "r", encoding="utf-8") as f:
    keybinds = json.load(f)
       
# Main prefs
set_appearance_mode("system")
set_default_color_theme("green")

class Window(CTk):
    def __init__(self, width, height, keys, binds) -> None:
        super().__init__()

        self.f_keys = keys
        self.keybinds = binds

        # shirina
        self.width = width

        # visota
        self.height = height

        # App title and geometry
        self.title("Custom Keybinds")
        self.geometry(f"{self.width}x{self.height}")

        # App grid
        # self.grid_columnconfigure((1,2,3,4,5), weight=1)
        # self.grid_rowconfigure((1,2,3,4,5), weight=1)
        
        self.dropdowns = []
        
        self.create_dropdowns()

        self.main_menu()

    def create_dropdowns(self):
        keyamount = len(self.f_keys)
        for i in range(keyamount):
            droplabel = CTkLabel(self, text=list(self.f_keys.keys())[i], font=CTkFont(family="Nunito", size=20))
            dropdown = CTkComboBox(self, values=list(self.keybinds.keys()), font=CTkFont(family="Nunito", size=20), width=200)
            if i < keyamount/2:
                droplabel.grid(row=i+3, column=1, padx=10, pady=10)
                dropdown.grid(row=i+3, column=2, padx=10, pady=10)
            elif i >= keyamount/2:
                droplabel.grid(row=i+3-int(keyamount/2), column=4, padx=10, pady=10)
                dropdown.grid(row=i+3-int(keyamount/2), column=5, padx=10, pady=10)
            self.dropdowns.append(dropdown)

    def main_menu(self):
        self.text = CTkLabel(self, text="Keybinds", font=CTkFont(family="Nunito", size=60))
        self.text.grid(row=0, column=0, padx=20, pady=20)
        self.hren = CTkFrame(self, fg_color="transparent")
        self.hren.grid(row=0, column=3, rowspan=5)
        
        from backend.main import leegoo
        self.bind_everything = CTkButton(self, text="Bind!", command=leegoo)
        self.bind_everything.grid(row=0, column=1, padx=20, pady=20)

if __name__ == "__main__":   
    app = Window(1280, 720, f_keys, keybinds)
    app.mainloop()