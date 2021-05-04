def main():
    from pyperclip import copy as cpy
    import pyautogui
    from time import sleep

    def gg():
        sleep(3)
        cpy('!p gooba earrape')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        cpy('-p gooba earrape')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        cpy('!loop')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        cpy('-loop')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    gg()

if __name__ == '__main__':
    main()