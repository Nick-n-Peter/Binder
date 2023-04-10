import pyautogui
from typing import Optional
from logging import basicConfig as logger_cfg
from logging import INFO as BASIC
from logging import info as logwriter
import keyboard

class ScreenRes():
    def __init__(self) -> None:
        pass
    
    def get(self) -> tuple:
        width, height = pyautogui.size()
        return width, height
    
class BindKey():
    def __init__(self, key: str, func: str, logger: Optional[bool]=False, logdir: Optional[str]='./Keybind.log') -> None:
        if key == None or key == "":
            raise ValueError("You have to specify a key!")
        if func == None or function == "":
            raise ValueError("You have to specify function for a key!")
        if logger:
            logger_cfg(filename=logdir, level=BASIC)
            print(f"Created logger at {logdir} for BindKey")
            logwriter(f"[BindKey] Requested logger at {logdir}")
        self.key = key
        self.func = func
    
    async def bind(self):
        while True:
            try:
                pressed = keyboard.is_pressed(self.key)
            except:
                pass
        if pressed:
            pass