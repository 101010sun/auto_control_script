from cellphone_controller_android import AndroidCellphoneController
from dotenv import load_dotenv
import os
import time

# 載入環境變數
load_dotenv()

class SamSungS20FEController(AndroidCellphoneController):
    def _clean_up(self):
        os.system(f"adb shell input tap 238 2332")
        time.sleep(0.5)
        os.system(f"adb shell input tap 525 1880")
        return
    

    def watch_predefined_youtube_videos(self, playTime: int):
        return super().watch_predefined_youtube_videos(playTime)
    

    def download_web_file(self):
        return super().download_web_file()
    

    def play_spotify_music(self, playTime: int):
        return super().play_spotify_music(playTime)
    

    def join_google_meet(self, playTime: int):
        room = os.environ.get("GOOGLE_MEET_ROOM") # 會議室代碼
        os.system(f"adb shell am start https://meet.google.com/{room}")
        time.sleep(1)
        os.system(f"adb shell input tap 400 700") # 選擇第一個帳戶
        time.sleep(5) # 等待設定
        os.system(f"adb shell input tap 520 1962") # 加入會議
        time.sleep(playTime) # 會議時長 
        os.system(f"adb shell input tap 152 2124") # 離開會議
        time.sleep(1)
        self._clean_up()
        return