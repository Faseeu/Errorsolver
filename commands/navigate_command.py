from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def navigate_to_line(line):
    # This assumes VS Code is already open and focused on the file
    keyboard.press(Key.ctrl)
    keyboard.press('g')
    keyboard.release('g')
    keyboard.release(Key.ctrl)
    time.sleep(0.5)
    keyboard.type(str(line))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
