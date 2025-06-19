
from pynput.keyboard import Key, Listener

list1 = []

def on_press(key):
    try:
        list1.append(key.char)
    except AttributeError:
        list1.append(key)
