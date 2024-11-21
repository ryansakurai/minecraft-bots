import time
import pyautogui as gui
import keyboard

def main():
    for sec in range(1, 6):
        time.sleep(1)
        print(sec)

    build_up = [True]
    gui.mouseDown(button='right')
    gui.keyDown("space")

    def change_mode(_):
        gui.mouseUp(button='right')
        gui.keyUp("space")
        build_up[0] = False
    keyboard.on_press_key(",", change_mode)

    while build_up[0]:
        time.sleep(1)

    tear_down = [True]
    gui.mouseDown(button='left')

    def exit_bot(_):
        gui.mouseUp(button='left')
        tear_down[0] = False
    keyboard.on_press_key(".", exit_bot)

    while tear_down[0]:
        time.sleep(1)


if __name__ == "__main__":
    main()
