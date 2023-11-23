from dotenv import load_dotenv
import uiautomation as auto
import os
import random
import json
import time
import subprocess

# 載入環境變數
load_dotenv()

class WindowsComputerController:
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
        smallWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        smallWindow.ButtonControl(searchDepth=6, Name="訪客模式").Click()
        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(youtube_video_list[random_index] + '{Enter}')
        time.sleep(playTime)
        chromeWindow.SendKeys('{ALT}{F4}')
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
        smallWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        smallWindow.ButtonControl(searchDepth=6, Name="訪客模式").Click()

        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(web_download_list[random_index] + '{Enter}')
        
        saveFileWindow = auto.WindowControl(searchDepth=2, Name="另存新檔")
        saveFileWindow.ButtonControl(searchDepth=2, Name="存檔(S)").Click()
        time.sleep(20)
        chromeWindow.SendKeys('{ALT}{F4}')
        return
    

    def play_spotify_music(self, playTime: int):
        playlistName = os.environ.get("SPOTIFY_PLAYLIST_NAME")  # 播放清單名稱
        
        subprocess.Popen('Spotify.exe') # 執行 Spotify
        spotifyWindow = auto.PaneControl(searchDepth=1, ClassName='Chrome_WidgetWin_0') # 連接 Spotify 視窗
        spotifyWindow.HyperlinkControl(searchDepth=11, Name='搜尋').Click()
        spotifyWindow.EditControl(searchDepth=12, Name='想聽什麼？').SendKeys(playlistName)
        spotifyWindow.HyperlinkControl(searchDepth=19, Name=playlistName).Click()
        playButton = spotifyWindow.ButtonControl(searchDepth=21, Name=f'播放 {playlistName}')
        playButton.Click() # 播放
        time.sleep(playTime)
        playButton.Click() # 停止
        spotifyWindow.HyperlinkControl(searchDepth=11, Name='搜尋').Click()
        spotifyWindow.SendKeys('{ALT}{F4}')
        return
    

    def join_google_meet(self):
        googleMeetUrl = os.environ.get("GOOGLE_MEET_URL")
        googleMeetRoom = os.environ.get("GOOGLE_MEET_ROOM")
        subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe') # 執行 Chrome
        smallWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        smallWindow.ButtonControl(searchDepth=6, Name="訪客模式").Click()

        chromeWindow = auto.PaneControl(searchDepth=1, ClassName="Chrome_WidgetWin_1")
        chromeWindow.EditControl(searchDepth=9, Name="網址與搜尋列").SendKeys(googleMeetUrl + '{Enter}')
        chromeWindow.EditControl(searchDepth=6, Name='Enter meeting code').SendKeys(googleMeetRoom + '{Enter}')
        chromeWindow.ButtonControl(searchDepth=10, Name="允許使用麥克風").Click()
        chromeWindow.ButtonControl(searchDepth=7, Name='允許').Click()
        chromeWindow.EditControl(searchDepth=13, Name='你的名稱').SendKeys('Test')
        chromeWindow.ButtonControl(searchDepth=12, Name='要求加入').Click()

        return


    def send_gmail(self):
        return
    

    def view_specific_webpages(self, playTime: int):
        # 取得 predefined webpage url
        web_webpage_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            web_webpage_list = file["web_webpage_list"]

        # 隨機選擇瀏覽的網頁頁面
        random_index = random.randint(0, len(web_webpage_list)-1)
        os.system(f"adb shell am start {web_webpage_list[random_index]}")
        time.sleep(playTime)
        return
    

    def start_skype_call(self, playTime: int):
        subprocess.Popen('Skype.exe')
        skypeWindow = auto.WindowControl(searchDepth=1, Name='Skype')
        text = skypeWindow.TextControl(searchDepth=0, Name='人員、群組、訊息、網路')
        print(text)
        text.Click()
        # searchSkype = skypeWindow.EditControl(searchDepth=0, Name='搜尋 Skype')
        # searchSkype.SendKeys('wpa3_testing')
        return
    

    def upload_google_drive_file(self):
        return


    def download_google_drive_file(self):
        return
    
