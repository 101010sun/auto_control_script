from base.logger import Logger
import random
import time
import pyautogui
import json

def test_youtube():
    youtube_video_list = []
    with open("url_list.json", "r") as f:
        file = json.load(f)
        youtube_video_list = file["youtube_video_list"]

    random_index = random.randint(0, len(youtube_video_list)-1)
    pyautogui.click(10, 15, duration=1)  # 選單
    pyautogui.click(84, 53, duration=1)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.click(172, 96, duration=1)  # 網址列
    pyautogui.typewrite(youtube_video_list[random_index])
    pyautogui.press('enter')
    time.sleep(2)
    time.sleep(10) # play time

    pyautogui.click(951, 574, duration=1)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return

def test_download_web_file():
    web_download_list = []
    with open("url_list.json", "r") as f:
        file = json.load(f)
        web_download_list = file["web_download_list"]
    random_index = random.randint(0, len(web_download_list)-1)

    pyautogui.click(10, 15, duration=0.5)  # 選單
    pyautogui.click(84, 53, duration=0.3)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.3)  # 網址列
    pyautogui.typewrite(web_download_list[random_index])
    pyautogui.press('enter')
    time.sleep(1)
    time.sleep(10)

    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    time.sleep(0.3)
    pyautogui.click(1126, 233, duration=0.2) # 未下載完須點選結束
    return

def main():
    test_download_web_file()


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    main()
