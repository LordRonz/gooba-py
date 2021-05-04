from pyperclip import copy as cpy
import pyautogui

ph = pyautogui.hotkey
pp = pyautogui.press

def wowee(s):
    cpy(s)
    ph('ctrl', 'v')
    pp('enter')

def groovy(title):
    wowee(f'-p {title}')
    wowee('-loop track')

def rythm(title):
    wowee(f'!pt {title}')
    wowee('!loop')

def fredboat(title):
    wowee(f';;p {title}')
    wowee(';;p 1')
    wowee(';;loop all')

def octave(title):
    wowee(f'_p {title}')
    wowee('_loop song')

def hydra(title):
    wowee(f'.p {title}')

def vexera(title):
    wowee(f'+p {title}')
    wowee('+repeat one')

def _247(title):
    wowee(f'mb play {title}')