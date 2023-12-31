from dotenv import load_dotenv
from computer.computer_controller_windows import WindowsController
import uiautomation as auto
import pyautogui
import subprocess
import time
import json

# 載入環境變數
load_dotenv()


class AsusA550VController(WindowsController):
    def _clean_up(self, windows: auto.PaneControl or auto.WindowControl):
        return super()._clean_up(windows)

    def enable_wifi(self):
        pyautogui.click(1182, 742, clicks=1)  # 點選網路圖標
        time.sleep(2)
        pyautogui.click(1051, 699, clicks=1)  # 點選 wifi
        time.sleep(5)
        pyautogui.click(1182, 742, clicks=1)  # 收起網路清單
        return

    def disable_wifi(self):
        pyautogui.click(1182, 742, clicks=1)  # 點選網路圖標
        time.sleep(2)
        pyautogui.click(1051, 699, clicks=1)  # 點選 wifi
        time.sleep(5)
        pyautogui.click(1182, 742, clicks=1)  # 收起網路清單
        return

    def watch_predefined_youtube_videos(self, playTime: int):
        return super().watch_predefined_youtube_videos(playTime)

    def download_web_file(self, waitTime: int):
        return super().download_web_file(waitTime)

    def play_spotify_music(self, playTime: int):
        return super().play_spotify_music(playTime)

    def join_google_meet(self, waitTime: int):
        return super().join_google_meet(waitTime)

    def send_gmail(self):
        return super().send_gmail()

    def view_specific_webpages(self, playTime: int):
        return super().view_specific_webpages(playTime)

    def start_skype_call(self, playTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            skypeLink = self._get_json_data("skype_url")

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                skypeLink + '{Enter}')
            time.sleep(5)
            chromeWindow.ButtonControl(searchDepth=7, Name="取消").Click()
            chromeWindow.ButtonControl(searchDepth=8, Name="以來賓身分加入").Click()
            time.sleep(7)
            chromeWindow.EditControl(
                searchDepth=11, Name="輸入您的名稱").SendKeys('asusA550v_tester')
            time.sleep(1)

            pyautogui.moveTo(691, 445, duration=0.5)  # 滑鼠移到中間
            pyautogui.scroll(-100)  # 滾輪往下滑

            if chromeWindow.ButtonControl(searchDepth=13, Name="開始通話").Exists():
                chromeWindow.ButtonControl(searchDepth=13, Name="開始通話").Click()
            else:
                chromeWindow.ButtonControl(searchDepth=11, Name="加入通話").Click()

            time.sleep(2)
            time.sleep(playTime)
            self._clean_up(chromeWindow)
        return

    def upload_google_drive_file(self, waitTime: int):
        return super().upload_google_drive_file(waitTime)

    def download_google_drive_file(self, waitTime: int):
        return super().download_google_drive_file(waitTime)
