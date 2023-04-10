'''
python sandbox.py > fonts.txt
'''
from tkinter import font
from tkinter import Tk
root = Tk()
# list(font.families())
batch = []
for i, fontie in enumerate(list(font.families())):
    batch.append(fontie)
    if i%5 == 0:
        print(batch)
        batch = []