"""
Script for bringing wolves with you across an ocean.
"""
import time
import keyboard
import pyautogui as gui

flags = {
    "continue": True,
}


def main():
    countdown()

    def exit_bot(_):
        flags["continue"] = False
    keyboard.on_press_key(".", exit_bot)

    while flags["continue"]:
        row_a_little()

def countdown() -> None:
    for sec in range(1, 6):
        time.sleep(1)
        print(sec)

def row_a_little() -> None:
    gui.keyDown("w")
    time.sleep(0.01)
    gui.keyUp("w")
    time.sleep(2)


if __name__ == "__main__":
    main()
