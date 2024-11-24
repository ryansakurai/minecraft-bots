"""
Script for hitting skeletons in a farm.
"""
import time
import pyautogui as gui
import keyboard

flags = {
    "continue": True,
}


def main():
    countdown()

    def exit_bot(_):
        flags["continue"] = False
    keyboard.on_press_key(".", exit_bot)

    while flags["continue"]:
        hit_skeleton()

def countdown() -> None:
    for sec in range(1, 6):
        time.sleep(1)
        print(sec)

def hit_skeleton():
    gui.leftClick()
    time.sleep(0.25)


if __name__ == "__main__":
    main()
