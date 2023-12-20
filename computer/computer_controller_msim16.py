from dotenv import load_dotenv
from base import ControllerBase
import pyautogui
import subprocess
import time
import json

# 載入環境變數
load_dotenv()


class MsiM16Controller(ControllerBase):
    def _clean_up(self):
        pyautogui.moveTo()  # 移至筆電中心
        pyautogui.hotkey('alt', 'f4', interval=0.5)  # 關閉視窗
        return

    def get_cursor_position(self):
        time.sleep(2)
        print(pyautogui.position())

    def enable_wifi(self):
        return

    def disable_wifi(self):
        return

    def watch_predefined_youtube_videos(self, playTime: int):
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
