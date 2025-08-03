"""
Script for hitting skeletons in a farm.
"""
import time
import pyautogui as gui
import keyboard

SWORD_COOLDOWN = 0.25

class Hotbar:
    def __init__(self):
        self._curr_slot = 1
        gui.press("1")

    def next_slot(self):
        self._curr_slot = self._curr_slot % 9 + 1
        gui.press(str(self._curr_slot))

flags = {
    "continue": False,
}

def main():
    def start_bot(_):
        flags["continue"] = True
    keyboard.on_press_key(",", start_bot)

    def exit_bot(_):
        flags["continue"] = False
    keyboard.on_press_key(".", exit_bot)

    wait_start()
    hotbar = Hotbar()

    while flags["continue"]:
        hit_skeleton()
        hotbar.next_slot()
        time.sleep(SWORD_COOLDOWN)

def wait_start() -> None:
    while not flags["continue"]:
        time.sleep(1)

def hit_skeleton():
    gui.leftClick()


if __name__ == "__main__":
    main()
