from dotenv import load_dotenv
from base import ControllerBase
import os
import random
import time

# 載入環境變數
load_dotenv()


class AndroidCellphoneController(ControllerBase):
    def __init__(self, adb_name: str):
        self.adb_name = adb_name

    def _clean_up(self):
        return
    
    def _adb_shell_command(self, command: str):
        os.system(f"adb -s {self.adb_name} shell {command}")
        return

    def enable_wifi(self):
        self._adb_shell_command("svc wifi enable")
        time.sleep(8)
        return

    def disable_wifi(self):
        self._adb_shell_command("svc wifi disable")
        time.sleep(1)
        return

    def watch_predefined_youtube_videos(self, playTime: int):
        # 取得 predefined Youtube videos
        youtube_video_list = self._get_json_data("youtube_video_list")

        # 隨機選擇要瀏覽的影片
        random_index = random.randint(0, len(youtube_video_list)-1)
        self._adb_shell_command(f"am start {youtube_video_list[random_index]}")
        time.sleep(playTime)
        self._clean_up()
        return

    def download_web_file(self, waitTime: int):
        return

    def play_spotify_music(self, playTime: int):
        playlist = os.environ.get("SPOTIFY_PLAYLIST")  # 播放清單代碼
        self._adb_shell_command(f"am start -a android.intent.action.VIEW spotify:playlist:{playlist}:play")
        time.sleep(playTime)
        self._clean_up()
        return

    def join_google_meet(self, playTime: int):
        return

    def send_gmail(self):
        return

    def view_specific_webpages(self, playTime: int):
        # 取得 predefined webpage url
        web_webpage_list = self._get_json_data("web_webpage_list")

        # 隨機選擇瀏覽的網頁頁面
        random_index = random.randint(0, len(web_webpage_list)-1)
        self._adb_shell_command(f"am start {web_webpage_list[random_index]}")
        time.sleep(playTime)
        self._clean_up()
        return

    def start_skype_call(self, playTime: int):
        return

    def upload_google_drive_file(self, waitTime: int):
        return

    def download_google_drive_file(self, waitTime: int):
        return
