#STOP SHOUTING ALREADY - ComboDev April 2022
from pynput.keyboard import Key, Listener


def main(key):
    print(key)
    if key == Key.backspace:
        return False

with Listener(on_press = main) as listener:
    listener.join()