"""
Script for building up and tearing down a pile of gravel to get flints.
"""
import time
import pyautogui as gui
import keyboard

flags = {
        "build up": True,
        "tear down": False,
    }


def main():
    def change_mode(_):
        flags["build up"] = not flags["build up"]
        flags["tear down"] = not flags["tear down"]
    keyboard.on_press_key(",", change_mode)

    def exit_bot(_):
        flags["build up"] = flags["tear down"] = False
    keyboard.on_press_key(".", exit_bot)

    countdown()

    while flags["build up"] or flags["tear down"]:
        if flags["build up"]:
            build_up(True)
            wait("build up")
            build_up(False)

        if flags["tear down"]:
            tear_down(True)
            wait("tear down")
            tear_down(False)

def countdown() -> None:
    for sec in range(1, 6):
        time.sleep(1)
        print(sec)

def build_up(turn_on: bool) -> None:
    if turn_on:
        gui.mouseDown(button='right')
        gui.keyDown("space")
    else:
        gui.mouseUp(button='right')
        gui.keyUp("space")

def tear_down(turn_on: bool) -> None:
    if turn_on:
        gui.mouseDown(button='left')
    else:
        gui.mouseUp(button='left')

def wait(process: str) -> None:
    while flags[process]:
        time.sleep(1)


if __name__ == "__main__":
    main()
