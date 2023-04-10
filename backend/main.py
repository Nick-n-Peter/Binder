import json

# Appending root folder
import sys
sys.path.append('./')

from resources.classes import BindKey

with open('resources/keybinds.json') as f:
    dicty = json.load(f)

async def leegoo(dropdowns):
    for i, (dropdown) in enumerate(dropdowns):
        command = dropdown.get()
        keybind = BindKey(f'F{i+1}', command, True, dictionary=dicty)
        await keybind.bind()