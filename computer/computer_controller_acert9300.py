from pydoc import classname
from re import search
from dotenv import load_dotenv
import uiautomation as auto
import os
import random
import json
import time
import subprocess

# 載入環境變數
load_dotenv()

class AcerT9300Controller:
    def _clean_up(self, windows: auto.PaneControl or auto.WindowControl):
        windows.SendKeys('{ALT}{F4}')
        return
    

    def enable_wifi(self):
        return
    

    def disable_wifi(self):
        return 


    def watch_predefined_youtube_videos(self, playTime: int):
        # 取得 predefined Youtube videos
        youtube_video_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            youtube_video_list = file["youtube_video_list"]

        # 隨機選擇要瀏覽的影片
        random_index = random.randint(0, len(youtube_video_list)-1)
        
        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(youtube_video_list[random_index] + '{Enter}')
        time.sleep(2)
        chromeWindow.SendKeys('{Space}')
        time.sleep(playTime)
        self._clean_up(chromeWindow)
        return


    def download_web_file(self):
        # 取得 predefined nodejs and python download url
        web_download_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            web_download_list = file["web_download_list"]

        # 隨機選擇要下載 nodejs or python
        random_index = random.randint(0, len(web_download_list)-1)
        
        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(web_download_list[random_index] + '{Enter}')
        
        # # 不會跳另存新檔
        # try:
        #     saveFileWindow = auto.WindowControl(searchDepth=2, Name="另存新檔")
        #     saveFileWindow.ButtonControl(searchDepth=2, Name="存檔(S)").Click()
        # except LookupError:
        #     print('no save windows.')

        time.sleep(25) # 等待下載
        self._clean_up(chromeWindow)
        return
    

    def play_spotify_music(self, playTime: int):
        playlistName = os.environ.get("SPOTIFY_PLAYLIST_NAME")  # 播放清單名稱
        
        subprocess.Popen('Spotify.exe') # 執行 Spotify
        time.sleep(2)
        spotifyWindow = auto.PaneControl(searchDepth=1, ClassName='Chrome_WidgetWin_0') # 連接 Spotify 視窗
        spotifyWindow.HyperlinkControl(searchDepth=11, Name='搜尋').Click()
        spotifyWindow.EditControl(searchDepth=12, Name='想聽什麼？').SendKeys(playlistName)
        spotifyWindow.HyperlinkControl(searchDepth=19, Name=playlistName).Click()
        playButton = spotifyWindow.ButtonControl(searchDepth=21, Name=f'播放 {playlistName}')
        playButton.Click() # 播放
        time.sleep(playTime)
        playButton.Click() # 停止
        spotifyWindow.HyperlinkControl(searchDepth=11, Name='搜尋').Click()
        self._clean_up(spotifyWindow)
        return
    

    def join_google_meet(self):

        with open("url_list.json", "r") as f:
            file = json.load(f)
            googleMeetUrl = file["google_meet_url"]
        googleMeetRoom = os.environ.get("GOOGLE_MEET_ROOM")

        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(googleMeetUrl + '{Enter}')
        chromeWindow.EditControl(searchDepth=10, Name='輸入代碼或暱稱').SendKeys(googleMeetRoom + '{Enter}')
        time.sleep(5)

        # # 開啟開啟權限，開過一次之後就不用再允許了
        # try:
        #     chromeWindow.ButtonControl(searchDepth=10, Name="允許使用麥克風和攝影機").Click()
        #     chromeWindow.ButtonControl(searchDepth=7, Name='允許').Click()
        # except LookupError:
        #     print('permission had been accepted.')

        chromeWindow.ButtonControl(searchDepth=13, Name='立即加入').Click()
        time.sleep(20)
        chromeWindow.ButtonControl(searchDepth=11, Name='退出通話').Click()
        self._clean_up(chromeWindow)
        return


    def send_gmail(self):
        gmailDes = os.environ.get("GMAIL_DES")
        gmailSubject = os.environ.get("GMAIL_SUBJECT")
        gmailBody = os.environ.get("GMAIL_BODY")
        newMail = "?compose=new"

        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.TextControl(searchDepth=13, Name="Gmail").Click() # 進入 gmail
        time.sleep(2) # 等待 init
        search = chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列")
        search.Click()
        search.SendKeys('{End}')
        search.SendKeys(newMail)
        search.SendKeys('{Enter}') # 新增郵件
        time.sleep(2)
        chromeWindow.ComboBoxControl(searchDepth=17, Name='').SendKeys(gmailDes)
        chromeWindow.EditControl(searchDepth=10, Name="主旨").SendKeys(gmailSubject)
        chromeWindow.EditControl(searchDepth=20, Name='郵件內文').SendKeys(gmailBody)
        chromeWindow.ButtonControl(searchDepth=16, Name="傳送 \u202a(Ctrl-Enter)\u202c").Click()
        time.sleep(3) # 傳送郵件
        self._clean_up(chromeWindow)
        return
    

    def view_specific_webpages(self, playTime: int):
        # 取得 predefined webpage url
        web_webpage_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            web_webpage_list = file["web_webpage_list"]

        # 隨機選擇瀏覽的網頁頁面
        random_index = random.randint(0, len(web_webpage_list)-1)
        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(web_webpage_list[random_index] + '{Enter}')
        time.sleep(2) # 網頁 loading
        time.sleep(playTime)
        self._clean_up(chromeWindow)
        return
    

    def start_skype_call(self, playTime: int):
        with open("url_list.json", "r") as f:
            file = json.load(f)
            skypeLink = file["skype_url"]

        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(skypeLink + '{Enter}')
        time.sleep(5)
        chromeWindow.ButtonControl(searchDepth=7, Name="開啟「Skype」").Click()
        time.sleep(2)

        # subprocess.Popen('Skype.exe')
        # time.sleep(2)
        # skypeWindow = auto.PaneControl(searchDepth=1, Name='Skype', ClassName="Chrome_WidgetWin_1")
        # text = skypeWindow.TextControl(searchDepth=0, Name='人員、群組、訊息、網路')
        # print(text)
        # text.Click()
        # searchSkype = skypeWindow.EditControl(searchDepth=0, Name='搜尋 Skype')
        # searchSkype.SendKeys('wpa3_testing')
        return
    

    def upload_google_drive_file(self):
        with open("url_list.json", "r") as f:
            file = json.load(f)
            google_drive_url = file["google_drive_url"]

        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        time.sleep(2)
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(google_drive_url + '{Enter}')
        time.sleep(1)
        chromeWindow.MenuItemControl(searchDepth=6, Name="新增").Click() # 點選新增
        chromeWindow.MenuItemControl(searchDepth=5, Name="檔案上傳").Click() # 點選檔案上傳
        time.sleep(1)
        chromeWindow.ListItemControl(searchDepth=8, Name=f"{os.environ.get('GOOGLE_DRIVE_FILE')}").Click() # 點選文件
        chromeWindow.ButtonControl(searchDepth=3, Name="開啟(O)").Click() # 開啟
        time.sleep(10)
        self._clean_up(chromeWindow)
        return


    def download_google_drive_file(self):
        return
    
