"""
Script for hitting skeletons in a farm.
"""
import time
import pyautogui as gui
import keyboard

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

    while flags["continue"]:
        hit_skeleton()

def wait_start() -> None:
    while not flags["continue"]:
        time.sleep(1)

def hit_skeleton():
    gui.leftClick()
    time.sleep(0.25)


if __name__ == "__main__":
    main()
