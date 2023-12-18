from dotenv import load_dotenv
from computer.computer_controller_windows import WindowsController
import uiautomation as auto
import os
import random
import json
import time
import subprocess

# 載入環境變數
load_dotenv()

class AsusA550VController(WindowsController):
    def _clean_up(self, windows: auto.PaneControl or auto.WindowControl):
        return super()._clean_up(windows)
    

    def enable_wifi(self):
        return
    

    def disable_wifi(self):
        return 


    def watch_predefined_youtube_videos(self, playTime: int):
        return super().watch_predefined_youtube_videos(playTime)


    def download_web_file(self):
        return super().download_web_file()
    

    def play_spotify_music(self, playTime: int):
        return super().play_spotify_music(playTime)
    

    def join_google_meet(self):
        return super().join_google_meet()


    def send_gmail(self):
        return super().send_gmail()
    

    def view_specific_webpages(self, playTime: int):
        return super().view_specific_webpages(playTime)
    

    def start_skype_call(self, playTime: int, joinName: str):
        return super().start_skype_call(playTime, joinName)
        return
    

    def upload_google_drive_file(self):
        return super().upload_google_drive_file()


    def download_google_drive_file(self):
        return super().download_google_drive_file()
    
