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
    time.sleep(5)
    pyautogui.click(1248, 698, duration=0.2) # 立即加入
    time.sleep(10)
    pyautogui.click(1145, 1163, duration=0.3) # 退出通話
    time.sleep(0.2)
    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return 
    
def test_web():
    with open("url_list.json", "r") as f:
        file = json.load(f)
        web_webpage_list = file["web_webpage_list"]
    random_index = random.randint(0, len(web_webpage_list)-1)

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(web_webpage_list[random_index])
    pyautogui.press('enter')
    time.sleep(2)

    time.sleep(10)

    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return

def test_gmail():
    gmailDes = os.environ.get("GMAIL_DES")
    gmailSubject = os.environ.get("GMAIL_SUBJECT")
    gmailBody = os.environ.get("GMAIL_BODY")
    newMail = "?compose=new"
    with open("url_list.json", "r") as f:
        file = json.load(f)
        gmailUrl = file["gmail_url"]

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(f"{gmailUrl}{newMail}")
    pyautogui.press('enter')
    time.sleep(2)

    time.sleep(3)
    pyautogui.click(1350, 641, duration=0.3)  # 收件者
    pyautogui.typewrite(gmailDes)
    pyautogui.click(1358, 682, duration=0.3)
    pyautogui.click(1341, 710, duration=0.3)  # 主旨
    pyautogui.typewrite(gmailSubject)
    pyautogui.click(1302, 745, duration=0.3)  # 內文
    pyautogui.typewrite(gmailBody)
    pyautogui.click(1294, 1165, duration=0.3)  # 傳送

    time.sleep(3)
    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return

def test_upload_file():
    with open("url_list.json", "r") as f:
        file = json.load(f)
        google_drive_url = file["google_drive_url"]

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(google_drive_url)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.click(69, 222, duration=0.2)  # 點選新增
    pyautogui.click(88, 261, duration=0.2)  # 點選檔案上傳
    pyautogui.click(420, 203, duration=1)  # 家目錄
    pyautogui.click(693, 579, duration=0.5)
    pyautogui.click(1502, 1031, duration=0.2)  # 開啟
    time.sleep(20)

    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return
 
def test_download_file():
    with open("url_list.json", "r") as f:
        file = json.load(f)
        google_drive_url = file["google_drive_donwload_folder_url"]

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(google_drive_url)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.click(1708, 371, duration=1)
    time.sleep(25)

    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return

def test_skype():
    with open("url_list.json", "r") as f:
        file = json.load(f)
        skypeLink = file["skype_url"]

    pyautogui.click(10, 15, duration=0.3)  # 選單
    pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
    pyautogui.typewrite("Google Chrome")  # 開啟 chrome
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.click(172, 96, duration=0.2)  # 網址列
    pyautogui.typewrite(skypeLink)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.click(1001, 294, duration=1)  # 取消
    pyautogui.click(973, 653, duration=0.5)  # 以來賓的身分加入
    time.sleep(15)
    pyautogui.click(844, 827, duration=0.5)  # 加入名稱
    pyautogui.typewrite("msiM16_tester")
    pyautogui.click(1091, 921, duration=0.5)  # 開始通話
    time.sleep(25)

    pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
    pyautogui.hotkey('alt', 'F4')  # 關閉視窗
    return

def enable_wifi():
    wlan = os.environ.get("MSI_WLAN")
    os.system(f"sudo ip link set dev {wlan} up")
    time.sleep(5)
    return

def disable_wifi():
    wlan = os.environ.get("MSI_WLAN")
    os.system(f"sudo ip link set dev {wlan} down")
    return

def main():
    disable_wifi()
    print('sleep 15 s')
    enable_wifi()


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    main()
