import json

# Appending root folder
import sys
sys.path.append('./')

from frontend.app import Window
from resources.classes import BindKey

with open('resources/keybinds.json') as f:
    dicty = json.load(f)

def leegoo():
    for i, (dropdown) in enumerate(Window.dropdowns):
        command = dropdown.get()
        keybind = BindKey(f'F{i+1}', command, True, dictionary=dicty)
        keybind.bind()