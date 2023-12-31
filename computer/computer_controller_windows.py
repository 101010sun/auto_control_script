from dotenv import load_dotenv
from base import ControllerBase
import uiautomation as auto
import os
import random
import time
import subprocess

# 載入環境變數
load_dotenv()


class WindowsController(ControllerBase):
    def _clean_up(self, windows: auto.PaneControl or auto.WindowControl):
        windows.SendKeys('{ALT}{F4}')
        return

    def enable_wifi(self):
        return

    def disable_wifi(self):
        return

    def watch_predefined_youtube_videos(self, playTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            # 取得 predefined Youtube videos
            youtube_video_list: list = self._get_json_data("youtube_video_list")

            # 隨機選擇要瀏覽的影片
            random_index = random.randint(0, len(youtube_video_list)-1)

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                youtube_video_list[random_index] + '{Enter}')
            time.sleep(2)
            chromeWindow.SendKeys('{Space}')
            time.sleep(playTime)
            self._clean_up(chromeWindow)
        return

    def download_web_file(self, waitTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            # 取得 predefined nodejs and python download url
            web_download_list = self._get_json_data("web_download_list")

            # 隨機選擇要下載 nodejs or python
            random_index = random.randint(0, len(web_download_list)-1)

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                web_download_list[random_index] + '{Enter}')

            time.sleep(waitTime)  # 等待下載
            self._clean_up(chromeWindow)

            if chromeWindow.ButtonControl(searchDepth=7, Name="結束").Exists():
                chromeWindow.ButtonControl(searchDepth=7, Name="結束").Click()

        return

    def play_spotify_music(self, playTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            playlistName = os.environ.get("SPOTIFY_PLAYLIST_NAME")  # 播放清單名稱

            subprocess.Popen('Spotify.exe')  # 執行 Spotify
            time.sleep(2)
            spotifyWindow = auto.PaneControl(
                searchDepth=1, ClassName='Chrome_WidgetWin_0')  # 連接 Spotify 視窗
            spotifyWindow.HyperlinkControl(searchDepth=11, Name='搜尋').Click()
            spotifyWindow.EditControl(
                searchDepth=12, Name='想聽什麼？').SendKeys(playlistName)
            spotifyWindow.HyperlinkControl(
                searchDepth=19, Name=playlistName).Click()
            playButton = spotifyWindow.ButtonControl(
                searchDepth=21, Name=f'播放 {playlistName}')
            playButton.Click()  # 播放
            time.sleep(playTime)
            playButton.Click()  # 停止
            spotifyWindow.HyperlinkControl(searchDepth=11, Name='搜尋').Click()
            self._clean_up(spotifyWindow)
        return

    def join_google_meet(self, playTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            googleMeetRoom = os.environ.get("GOOGLE_MEET_ROOM")
            googleMeetUrl = self._get_json_data("google_meet_url")

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                googleMeetUrl + '{Enter}')
            chromeWindow.EditControl(searchDepth=10, Name='輸入代碼或暱稱').SendKeys(
                googleMeetRoom + '{Enter}')
            time.sleep(7)

            chromeWindow.ButtonControl(searchDepth=13, Name='立即加入').Click()
            time.sleep(playTime)
            chromeWindow.ButtonControl(searchDepth=11, Name='退出通話').Click()
            self._clean_up(chromeWindow)
        return

    def send_gmail(self):
        with auto.UIAutomationInitializerInThread(debug=True):
            gmailDes = os.environ.get("GMAIL_DES")
            gmailSubject = os.environ.get("GMAIL_SUBJECT")
            gmailBody = os.environ.get("GMAIL_BODY")
            newMail = "?compose=new"

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.TextControl(
                searchDepth=13, Name="Gmail").Click()  # 進入 gmail
            time.sleep(5)  # 等待 init
            search = chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列")
            search.Click()
            search.SendKeys('{End}')
            search.SendKeys(newMail)
            search.SendKeys('{Enter}')  # 新增郵件
            time.sleep(2)
            chromeWindow.ComboBoxControl(
                searchDepth=17, Name='').SendKeys(gmailDes)
            chromeWindow.EditControl(
                searchDepth=10, Name="主旨").SendKeys(gmailSubject)
            chromeWindow.EditControl(
                searchDepth=20, Name='郵件內文').SendKeys(gmailBody)
            chromeWindow.ButtonControl(
                searchDepth=16, Name="傳送 \u202a(Ctrl-Enter)\u202c").Click()
            time.sleep(5)  # 傳送郵件
            self._clean_up(chromeWindow)
        return

    def view_specific_webpages(self, playTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            # 取得 predefined webpage url
            web_webpage_list = self._get_json_data("web_webpage_list")

            # 隨機選擇瀏覽的網頁頁面
            random_index = random.randint(0, len(web_webpage_list)-1)
            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                web_webpage_list[random_index] + '{Enter}')
            time.sleep(2)  # 網頁 loading
            time.sleep(playTime)
            self._clean_up(chromeWindow)
        return

    def start_skype_call(self, playTime: int):
        return

    def upload_google_drive_file(self, waitTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            google_drive_url = self._get_json_data("google_drive_url")

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                google_drive_url + '{Enter}')
            time.sleep(1)
            chromeWindow.MenuItemControl(searchDepth=6, Name="新增").Click()  # 點選新增
            chromeWindow.MenuItemControl(
                searchDepth=5, Name="檔案上傳").Click()  # 點選檔案上傳
            time.sleep(1)
            chromeWindow.ListItemControl(
                searchDepth=8, Name=f"{os.environ.get('GOOGLE_DRIVE_FILE')}.docx").Click()  # 點選文件
            chromeWindow.ButtonControl(searchDepth=3, Name="開啟(O)").Click()  # 開啟
            time.sleep(waitTime)
            self._clean_up(chromeWindow)
        return

    def download_google_drive_file(self, waitTime: int):
        with auto.UIAutomationInitializerInThread(debug=True):
            google_drive_url = self._get_json_data("google_drive_donwload_folder_url")

            subprocess.Popen(
                'C:\Program Files\Google\Chrome\Application\chrome.exe')  # 執行 Chrome
            time.sleep(2)
            chromeWindow = auto.PaneControl(
                searchDepth=1, ClassName="Chrome_WidgetWin_1")
            chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(
                google_drive_url + '{Enter}')
            time.sleep(1)
            chromeWindow.TextControl(
                searchDepth=18, Name=f"{os.environ.get('GOOGLE_DRIVE_FILE')}.docx").RightClick()  # 按文件檔案右鍵
            chromeWindow.MenuItemControl(searchDepth=5, Name="下載").Click()
            time.sleep(waitTime)
            self._clean_up(chromeWindow)
        return
