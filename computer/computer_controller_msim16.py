from dotenv import load_dotenv
from base import ControllerBase
import pyautogui
import time
import os
import random

# 載入環境變數
load_dotenv()


class MsiM16Controller(ControllerBase):
    def _clean_up(self):
        pyautogui.click(951, 574, duration=0.5)  # 移至筆電中心
        pyautogui.hotkey('alt', 'F4')  # 關閉視窗
        return

    def get_cursor_position(self):
        time.sleep(2)
        print(pyautogui.position())
        return 

    def enable_wifi(self):
        wlan = os.environ.get("MSI_WLAN")
        os.system(f"sudo ip link set dev {wlan} up")
        time.sleep(5)
        return

    def disable_wifi(self):
        wlan = os.environ.get("MSI_WLAN")
        os.system(f"sudo ip link set dev {wlan} down")
        return

    def _open_application(self, appName: str, url: str = ""):
        pyautogui.click(10, 15, duration=0.3)  # 選單
        pyautogui.click(84, 53, duration=0.2)  # 選單搜尋
        pyautogui.typewrite(appName)  # 開啟 chrome
        pyautogui.press('enter')
        time.sleep(1)  # 等待開啟

        if appName == "Google Chrome" and url != "":
            pyautogui.click(172, 96, duration=0.2)  # 網址列
            pyautogui.typewrite(url)
            pyautogui.press('enter')
            time.sleep(5) # 等待網頁載入
        return 
    
    def watch_predefined_youtube_videos(self, playTime: int):
        # 取得 predefined Youtube videos
        youtube_video_list: list = self._get_json_data("youtube_video_list")

        # 隨機選擇要瀏覽的影片
        random_index = random.randint(0, len(youtube_video_list)-1)

        self._open_application("Google Chrome", youtube_video_list[random_index])
        time.sleep(playTime)
        self._clean_up
        return

    def download_web_file(self, waitTime: int):
        # 取得 predefined nodejs and python download url
        web_download_list: list = self._get_json_data("web_download_list")
        
        # 隨機選擇要下載 nodejs or python
        random_index = random.randint(0, len(web_download_list)-1)

        self._open_application("Google Chrome", web_download_list[random_index])
        time.sleep(waitTime) # 等待下載
        self._clean_up()
        time.sleep(0.3)
        pyautogui.click(1126, 233, duration=0.2) # 未下載完須點選結束
        return

    def play_spotify_music(self, playTime: int):
        playlistCode = os.environ.get("SPOTIFY_PLAYLIST")  # 播放清單代碼
        spotify_url: str = self._get_json_data("spotify_url")
        
        self._open_application("Google Chrome", f"{spotify_url}/playlist/{playlistCode}")
        pyautogui.click(485, 531, duration=0.3)  # 播放
        time.sleep(playTime)
        pyautogui.click(485, 531)  # 停止
        time.sleep(0.2)
        self._clean_up()
        return

    def join_google_meet(self, playTime: int):
        googleMeetRoom = os.environ.get("GOOGLE_MEET_ROOM")
        googleMeetUrl: str = self._get_json_data("google_meet_url")

        self._open_application("Google Chrome", googleMeetUrl)
        pyautogui.click(350, 771, duration=0.3) # 會議代碼
        pyautogui.typewrite(googleMeetRoom)
        pyautogui.click(602, 768, duration=0.1) # 加入
        time.sleep(5)
        pyautogui.click(1248, 698, duration=0.2) # 立即加入
        time.sleep(playTime)
        pyautogui.click(1145, 1163, duration=0.3) # 退出通話
        time.sleep(0.2)
        self._clean_up()
        return

    def send_gmail(self):
        gmailUrl: str = self._get_json_data("gmail_url")
        gmailDes = os.environ.get("GMAIL_DES")
        gmailSubject = os.environ.get("GMAIL_SUBJECT")
        gmailBody = os.environ.get("GMAIL_BODY")
        newMail = "?compose=new"

        self._open_application("Google Chrome", f"{gmailUrl}{newMail}")
        time.sleep(2)
        pyautogui.click(1350, 641, duration=0.3)  # 收件者
        pyautogui.typewrite(gmailDes)
        pyautogui.click(1358, 682, duration=0.3)  # 點
        pyautogui.click(1341, 710, duration=0.3)  # 主旨
        pyautogui.typewrite(gmailSubject)
        pyautogui.click(1302, 745, duration=0.3)  # 內文
        pyautogui.typewrite(gmailBody)
        pyautogui.click(1294, 1165, duration=0.3)  # 傳送
        time.sleep(10)
        self._clean_up()
        return

    def view_specific_webpages(self, playTime: int):
        web_webpage_list = self._get_json_data("web_webpage_list")
        # 隨機選擇瀏覽的網頁頁面
        random_index = random.randint(0, len(web_webpage_list)-1)
        self._open_application("Google Chrome", web_webpage_list[random_index])
        time.sleep(playTime)
        self._clean_up()
        return

    def start_skype_call(self, playTime: int):
        skypeLink = self._get_json_data("skype_url")
        self._open_application("Google Chrome", skypeLink)
        pyautogui.click(1001, 294, duration=1)  # 取消
        pyautogui.click(973, 653, duration=0.5)  # 以來賓的身分加入
        time.sleep(15)
        pyautogui.click(844, 827, duration=0.5)  # 加入名稱
        pyautogui.typewrite("msiM16_tester")
        pyautogui.click(1091, 921, duration=0.5)  # 開始通話

        time.sleep(playTime)
        self._clean_up()
        return

    def upload_google_drive_file(self, waitTime: int):
        google_drive_url = self._get_json_data("google_drive_url")
        self._open_application("Google Chrome", google_drive_url)
        pyautogui.click(69, 222, duration=0.2)  # 點選新增
        pyautogui.click(88, 261, duration=0.2)  # 點選檔案上傳
        pyautogui.click(420, 203, duration=1)  # 家目錄
        pyautogui.click(693, 579, duration=0.5)
        pyautogui.click(1502, 1031, duration=0.2)  # 開啟
        time.sleep(waitTime)
        self._clean_up()
        return

    def download_google_drive_file(self, waitTime: int):
        google_drive_url = self._get_json_data("google_drive_donwload_folder_url")
        self._open_application("Google Chrome", google_drive_url)
        pyautogui.click(1708, 371, duration=1)
        time.sleep(waitTime)
        self._clean_up()
        return
