from cellphone.cellphone_controller_android import AndroidCellphoneController
from dotenv import load_dotenv
import os
import time

# 載入環境變數
load_dotenv()


class OppoReno7Controller(AndroidCellphoneController):
    def _clean_up(self):
        os.system(f"adb shell input tap 553 2378")
        time.sleep(0.5)
        os.system(f"adb shell input tap 278 2320")
        time.sleep(0.5)
        os.system(f"adb shell input tap 540 2093")
        return

    def enable_wifi(self):
        return super().enable_wifi()

    def disable_wifi(self):
        return super().disable_wifi()

    def watch_predefined_youtube_videos(self, playTime: int):
        return super().watch_predefined_youtube_videos(playTime)

    def download_web_file(self):
        return super().download_web_file()

    def play_spotify_music(self, playTime: int):
        playlist = os.environ.get("SPOTIFY_PLAYLIST")  # 播放清單代碼
        os.system(
            f"adb shell am start -a android.intent.action.VIEW spotify:playlist:{playlist}:play")
        time.sleep(5)
        os.system(f"adb shell input tap 955 1178")  # oppo 不會自動播放
        time.sleep(playTime)
        self._clean_up()
        return

    def join_google_meet(self, playTime: int):
        room = os.environ.get("GOOGLE_MEET_ROOM")  # 會議室代碼
        os.system(f"adb shell am start https://meet.google.com/{room}")
        time.sleep(5)
        os.system(f"adb shell input tap 556 1993")  # 加入會議
        time.sleep(playTime)  # 會議時長
        os.system(f"adb shell input tap 152 2168")  # 離開會議
        time.sleep(3)
        self._clean_up()
        return

    def send_gmail(self):
        des = os.environ.get('GMAIL_DES')
        subject = os.environ.get('GMAIL_SUBJECT')
        body = os.environ.get('GMAIL_BODY')

        os.system(
            f"adb shell am start -n com.google.android.gm/com.google.android.gm.ConversationListActivityGmail")
        time.sleep(1)
        os.system(f"adb shell input tap 842 2001")  # 點擊撰寫
        time.sleep(0.5)
        os.system(f"adb shell input keyboard text '{des}'")  # 輸入收件人
        time.sleep(0.5)
        os.system(f"adb shell input keyevent 66")  # enter
        time.sleep(0.5)
        os.system(f"adb shell input keyevent 66")  # enter
        time.sleep(0.5)
        os.system(f"adb shell input tap 249 872")  # 點擊主旨
        os.system(f"adb shell input keyboard text '{subject}'")  # 輸入主旨
        time.sleep(0.5)
        os.system(f"adb shell input keyevent 66")  # enter
        time.sleep(0.5)
        os.system(f"adb shell input keyboard text '{body}'")  # 輸入內文
        time.sleep(0.5)
        os.system(f"adb shell input tap 856 207")  # 點擊傳送
        time.sleep(3)
        self._clean_up()
        return

    def view_specific_webpages(self, playTime: int):
        return super().view_specific_webpages(playTime)

    def start_skype_call(self, playTime: int):
        skypeName = "wpa3_testing"

        os.system(
            f"adb shell am start -n com.skype.raider/com.skype4life.MainActivity")
        time.sleep(3)
        os.system(f"adb shell input tap 323 2216")  # 點擊通話
        time.sleep(0.5)
        os.system(f"adb shell input tap 194 375")  # 點擊搜尋
        time.sleep(0.5)
        os.system(f"adb shell input keyboard text '{skypeName}'")
        time.sleep(1)
        os.system(f"adb shell input tap 272 620")  # 點擊聯絡人
        time.sleep(1)
        os.system(f"adb shell input tap 1002 208")  # 點擊通話
        time.sleep(0.5)
        os.system(f"adb shell input tap 547 2081")  # 點擊立即開始
        time.sleep(3)
        os.system(f"adb shell input tap 334 2160")  # 點擊開啟麥克風
        time.sleep(0.5)
        os.system(f"adb shell input tap 537 2158")  # 點擊開啟鏡頭
        time.sleep(playTime)  # 通話時長
        os.system(f"adb shell input tap 481 1103")  # 點擊螢幕
        time.sleep(0.5)
        os.system(f"adb shell input tap 760 2167")  # 點擊結束通話
        time.sleep(0.5)
        self._clean_up()
        return

    def upload_google_drive_file(self):
        os.system(
            f"adb shell am start -n com.google.android.apps.docs/com.google.android.apps.docs.app.NewMainProxyActivity")
        time.sleep(1)
        os.system(f"adb shell input tap 845 1872")  # 點擊 +
        time.sleep(0.5)
        os.system(f"adb shell input tap 550 1717")  # 點擊上傳
        time.sleep(0.5)
        os.system(f"adb shell input tap 942 334")  # 點擊文件
        time.sleep(0.5)
        os.system(f"adb shell input tap 419 1061")  # 點擊第一份文件
        time.sleep(0.5)
        os.system(f"adb shell input tap 845 207")  # 點擊選取
        time.sleep(30)  # 等待上傳
        self._clean_up()
        return

    def download_google_drive_file(self):
        os.system(
            f"adb shell am start -n com.google.android.apps.docs/com.google.android.apps.docs.app.NewMainProxyActivity")
        time.sleep(1)
        os.system(f"adb shell input tap 954 2135")  # 點擊檔案
        time.sleep(0.5)
        os.system(f"adb shell input tap 313 615")  # 點擊第一個資料夾
        time.sleep(0.5)
        os.system(f"adb shell input tap 972 645")  # 點擊第一個文件的選項
        time.sleep(0.5)
        os.system(f"adb shell input tap 305 2173")
        time.sleep(30)  # 等待下載
        self._clean_up()
        return
