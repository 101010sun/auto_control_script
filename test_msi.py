from base.logger import Logger
import random
import time
import pyautogui
import json

def get_cursor_position():
        time.sleep(2)
        print(pyautogui.position())
        return 

def test_youtube():
    youtube_video_list = []
    with open("url_list.json", "r") as f:
        file = json.load(f)
        youtube_video_list = file["youtube_video_list"]

    random_index = random.randint(0, len(youtube_video_list)-1)
    pyautogui.click(10, 15)  # 選單
    pyautogui.click(84, 53)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.click(172, 96)  # 網址列
    pyautogui.typewrite(youtube_video_list[random_index])
    pyautogui.press('enter')
    time.sleep(2)
    time.sleep(10) # play time

    pyautogui.click(951, 574)  # 移至筆電中心
    pyautogui.hotkey('alt', 'f4', interval=0.5)  # 關閉視窗

    return

def main():
    test_youtube()


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    main()
