from dotenv import load_dotenv
from base import ControllerBase
import pyautogui
import subprocess
import time
import json
import os
import random

# 載入環境變數
load_dotenv()


class MsiM16Controller(ControllerBase):
    def _clean_up(self):
        pyautogui.click(951, 574)  # 移至筆電中心
        pyautogui.hotkey('alt', 'f4', interval=0.5)  # 關閉視窗
        return

    def get_cursor_position(self):
        time.sleep(2)
        print(pyautogui.position())
        return 

    def enable_wifi(self):
        wlan = os.environ.get("MSI_WLAN")
        os.system(f"sudo ip link set dev {wlan} up")
        return

    def disable_wifi(self):
        wlan = os.environ.get("MSI_WLAN")
        os.system(f"sudo ip link set dev {wlan} down")
        return

    def watch_predefined_youtube_videos(self, playTime: int):
        # 取得 predefined Youtube videos
        youtube_video_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            youtube_video_list = file["youtube_video_list"]

        # 隨機選擇要瀏覽的影片
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
        time.sleep(playTime)
        self._clean_up
        return

    def download_web_file(self):
        return

    def play_spotify_music(self, playTime: int):
        return

    def join_google_meet(self):
        return

    def send_gmail(self):
        return

    def view_specific_webpages(self, playTime: int):
        return

    def start_skype_call(self, playTime: int):
        return

    def upload_google_drive_file(self):
        return

    def download_google_drive_file(self):
        return
