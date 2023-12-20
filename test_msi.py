from base.logger import Logger
import random
import time
import pyautogui

def get_cursor_position():
        time.sleep(2)
        print(pyautogui.position())
        return 

def main():
    get_cursor_position()


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    main()
