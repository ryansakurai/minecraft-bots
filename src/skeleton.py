import time
import pyautogui as gui
import keyboard

def main():
    for sec in range(1, 6):
        time.sleep(1)
        print(sec)

    continue_bot = [True]

    def exit_bot(_):
        continue_bot[0] = False
    keyboard.on_press_key(".", exit_bot)

    while continue_bot[0]:
        gui.leftClick()
        time.sleep(0.25)


if __name__ == "__main__":
    main()
