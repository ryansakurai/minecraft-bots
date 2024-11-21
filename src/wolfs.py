import time
import pyautogui as gui

def main():
    for sec in range(5):
        time.sleep(1)
        print(sec)
    for _ in range(1_000_000_000):
        gui.keyDown("w")
        time.sleep(0.01)
        gui.keyUp("w")
        time.sleep(2)


if __name__ == "__main__":
    main()