import json

# Appending root folder
import sys
sys.path.append('./')
import asyncio
from resources.classes import BindKey

with open('resources/keybinds.json') as f:
    dicty = json.load(f)
print('inited backend')
async def leegoo(dropdowns):
    loop = asyncio.get_event_loop()
    for i, (dropdown) in enumerate(dropdowns):
        command = dropdown.get()
        keybind = BindKey(f'F{i+1}', command, True, dictionary=dicty)
        print("binded")
        await keybind.bind()
    loop.run_until_complete(asyncio.sleep(0))