from cellphone.cellphone_controller_android import AndroidCellphoneController
from dotenv import load_dotenv
import os
import time
import random

# 載入環境變數
load_dotenv()


class SamsungS20FEController(AndroidCellphoneController):
    def _clean_up(self):
        self._adb_shell_command(f"input tap 238 2332")
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 525 1880")
        return

    def enable_wifi(self):
        return super().enable_wifi()

    def disable_wifi(self):
        return super().disable_wifi()

    def watch_predefined_youtube_videos(self, playTime: int):
        return super().watch_predefined_youtube_videos(playTime)

    def download_web_file(self, waitTime: int):
        # 取得 predefined nodejs and python download url
        web_download_list = self._get_json_data("web_download_list")

        # 隨機選擇要下載 nodejs or python
        random_index = random.randint(0, len(web_download_list)-1)
        self._adb_shell_command(f"am start {web_download_list[random_index]}")
        time.sleep(2)
        self._adb_shell_command(f"input tap 938 1441")  # 再次下載
        time.sleep(waitTime)
        self._clean_up()
        return

    def play_spotify_music(self, playTime: int):
        return super().play_spotify_music(playTime)

    def join_google_meet(self, playTime: int):
        room = os.environ.get("GOOGLE_MEET_ROOM")  # 會議室代碼
        self._adb_shell_command(f"am start https://meet.google.com/{room}")
        time.sleep(1)
        self._adb_shell_command(f"input tap 400 700")  # 選擇第一個帳戶
        time.sleep(5)  # 等待設定
        self._adb_shell_command(f"input tap 520 1962")  # 加入會議
        time.sleep(playTime)  # 會議時長
        self._adb_shell_command(f"input tap 152 2124")  # 離開會議
        time.sleep(1)
        self._clean_up()
        return

    def send_gmail(self):
        des = os.environ.get('GMAIL_DES')
        subject = os.environ.get('GMAIL_SUBJECT')
        body = os.environ.get('GMAIL_BODY')

        self._adb_shell_command(f"am start -n com.google.android.gm/com.google.android.gm.ConversationListActivityGmail")
        time.sleep(1)
        self._adb_shell_command(f"input tap 766 2008")  # 點擊撰寫
        time.sleep(0.5)
        self._adb_shell_command(f"input keyboard text '{des}'")  # 輸入收件人
        self._adb_shell_command(f"input keyevent 66")  # enter
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 106 709")  # 點擊主旨
        self._adb_shell_command(f"input keyboard text '{subject}'")  # 輸入主旨
        self._adb_shell_command(f"input keyevent 66")  # enter
        time.sleep(0.5)
        self._adb_shell_command(f"input keyboard text '{body}'")  # 輸入內文
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 848 209")  # 點擊傳送
        time.sleep(0.5)
        self._clean_up()
        return

    def view_specific_webpages(self, playTime: int):
        return super().view_specific_webpages(playTime)

    def start_skype_call(self, playTime: int):
        skypeName = "wpa3_testing"

        self._adb_shell_command(f"am start -n com.skype.raider/com.skype4life.MainActivity")
        time.sleep(3)
        self._adb_shell_command(f"input tap 518 2177")  # 點擊通話
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 252 355")  # 點擊搜尋
        time.sleep(0.5)
        self._adb_shell_command(f"input keyboard text '{skypeName}'")
        time.sleep(1)
        self._adb_shell_command(f"input tap 330 617")  # 點擊聯絡人
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 963 197")  # 點擊通話
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 441 2083")  # 點擊立即開始
        time.sleep(3)
        self._adb_shell_command(f"input tap 347 2155")  # 點擊開啟麥克風
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 527 2169")  # 點擊開啟鏡頭
        time.sleep(playTime)  # 通話時長
        self._adb_shell_command(f"input tap 479 1581")  # 點擊螢幕
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 749 2145")  # 點擊結束通話
        time.sleep(0.5)
        self._clean_up()
        return

    def upload_google_drive_file(self, waitTime: int):
        self._adb_shell_command(f"am start -n com.google.android.apps.docs/com.google.android.apps.docs.app.NewMainProxyActivity")
        time.sleep(1)
        self._adb_shell_command(f"input tap 947 1856")  # 點擊 +
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 535 1706")  # 點擊上傳
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 932 307")  # 點擊文件
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 352 1035")  # 點擊第一份文件
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 853 184")  # 點擊選取
        time.sleep(waitTime)  # 等待上傳
        self._clean_up()
        return

    def download_google_drive_file(self, waitTime: int):
        self._adb_shell_command(f"am start -n com.google.android.apps.docs/com.google.android.apps.docs.app.NewMainProxyActivity")
        time.sleep(2)
        self._adb_shell_command(f"input tap 941 2110")  # 點擊檔案
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 236 825")  # 點擊第一個資料夾
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 462 864")  # 點擊第一個文件的選項
        time.sleep(0.5)
        self._adb_shell_command(f"input tap 569 2159")
        time.sleep(waitTime)  # 等待下載
        self._clean_up()
        return
