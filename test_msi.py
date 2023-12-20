from dotenv import load_dotenv
from base.logger import Logger
import random
import time
import pyautogui
import json
import os

# 載入環境變數
load_dotenv()


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

def test_spotify():
    playlistCode = os.environ.get("SPOTIFY_PLAYLIST")  # 播放清單名稱
        
    with open("url_list.json", "r") as f:
        file = json.load(f)
        spotify_url = file["spotify_url"]

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(f"{spotify_url}/playlist/{playlistCode}")
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.click(485, 531, duration=0.3)  # 播放
    time.sleep(10)
    pyautogui.click(485, 531)  # 停止
    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return

def test_meet():
    googleMeetRoom = os.environ.get("GOOGLE_MEET_ROOM")
    with open("url_list.json", "r") as f:
        file = json.load(f)
        googleMeetUrl = file["google_meet_url"]

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(googleMeetUrl)
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.click(350, 771, duration=0.3) # 會議代碼
    pyautogui.typewrite(googleMeetRoom)
    
    pyautogui.click(602, 768, duration=0.1) # 加入
    time.sleep(20)
    pyautogui.click(1145, 1163, duration=0.3) # 退出通話
    return 
    
def main():
    test_meet()


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    main()
