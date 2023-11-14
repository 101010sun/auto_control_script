import os
import random
import json

class AndroidCellphoneController:
    def watch_predefined_youtube_videos(self):
        # 取得 predefined Youtube videos
        youtube_video_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            youtube_video_list = file["youtube_video_list"]

        # 隨機選擇要瀏覽的影片
        random_index = random.randint(0, len(youtube_video_list)-1)
        os.system(f"adb shell am start {youtube_video_list[random_index]}")


    def download_web_file(self):
        # 取得 predefined nodejs and python download url
        web_download_list = []
        with open("url_list.json", "r") as f:
            file = json.load(f)
            web_download_list = file["web_download_list"]

        # 隨機選擇要下載 nodejs or python
        random_index = random.randint(0, len(web_download_list)-1)
        os.system(f"adb shell am start {web_download_list[random_index]}")
    

    def play_spotify_music(self):
        playlist = "4bfj9Go9YnSq7L4YeWTWeY" # 播放清單代碼
        os.system(f"adb shell am start -a android.intent.action.VIEW spotify:playlist:{playlist}:play")
    

    
