"""
Script for bringing wolves with you across a body of water.
"""
import time
import keyboard
import pyautogui as gui

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
        row_a_little()

def wait_start() -> None:
    while not flags["continue"]:
        time.sleep(1)

def row_a_little() -> None:
    gui.keyDown("w")
    time.sleep(0.01)
    gui.keyUp("w")
    time.sleep(2)


if __name__ == "__main__":
    main()
