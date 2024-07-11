from pynput.keyboard import Controller, Key

keyboard = Controller()

def apply_fix(suggestion):
    keyboard.type(suggestion)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
