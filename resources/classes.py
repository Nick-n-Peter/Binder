import pyautogui
from typing import Optional
from logging import basicConfig as logger_cfg
from logging import INFO as BASIC
from logging import info as logwriter
import keyboard
from asyncio import sleep as asleep
from pynput import keyboard

class ScreenRes():
    def __init__(self) -> None:
        pass
    
    def get(self) -> tuple:
        width, height = pyautogui.size()
        return width, height
    
class BindKey():
    def __init__(self, key: str, function: str, logger: Optional[bool]=False, logdir: Optional[str]='./Keybind.log', dictionary=dict) -> None:
        if key == None or key == "":
            raise ValueError("You have to specify a key!")
        if function == None or function == "":
            raise ValueError("You have to specify function for a key!")
        if function not in dictionary:
            raise ValueError("Specified function is not stated in your dictionary")
        
        if logger:
            logger_cfg(filename=logdir, level=BASIC)
            print(f"Created logger at {logdir} for BindKey")
            logwriter(f"[BindKey] Requested logger at {logdir}")
        
        self.key = key
        self.func = function
        self.dict = dictionary
    
    async def bind(self):
        while True:
            if keyboard.is_pressed(self.key):
                logwriter(f'[BindKey] Registered {self.key}. Executing {self.func}.')
                command = self.dict.get(self.func)
                if command is not None:
                    eval(command)
            await asleep(0.1)