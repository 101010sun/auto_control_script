from base import Logger
from base import ControllerBase
from dotenv import load_dotenv
from time import localtime
import time
import socket
import threading
import os
import pickle
import pyautogui
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


class ContactNode:
    def __init__(self, deviceName: str):
        self.logger = Logger('WPA3Dataset', 'contact_node')
        self.server_host = os.environ.get("CENTER_HOST")
        self.server_port = os.environ.get("CENTER_PORT")
        self.device = deviceName

        if deviceName == 'MSIM16':
            self.host = os.environ.get("MSI_HOST")
            self.port = os.environ.get("MSI_PORT")
            self.controller = MsiM16Controller()

        self.wifi_reopen_flag = False

    def connect_to_server(self, msg: str):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.server_host, self.server_port))  # 連接
            message = {'device': self.device, 'msg': msg}
            s.send(pickle.dumps(message))

            s.shutdown(2)  # 中斷連接
            s.close()  # 關閉
        return 0

    # 監聽 func.
    def wait_for_socket_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            while True:
                conn, address = s.accept()
                client_handler = threading.Thread(target=self.receive_socket_message,
                                                  args=(s, conn, address))  # 處理收到的請求
                client_handler.start()
                if not client_handler.is_alive():
                    client_handler.join()
                    break
            s.shutdown(2)
            s.close()

    # 處理請求 func.
    def receive_socket_message(self, s: socket.socket, connection: socket.socket, address: socket._RetAddress):
        with connection:
            message = connection.recv(1024)  # 接收 msg
            try:
                parsed_msg = pickle.loads(message)  # 轉譯 msg
            except Exception:
                self.logger.logMsg(f"{message} cannot be parsed")
            self.logger.logMsg(f"Received: {parsed_msg}")

            if message:
                # server 傳送 執行正常流量指令
                if parsed_msg['msg'] == "normal_flow":
                    scenario = int(parsed_msg['scenario'])
                    self.controller.process_scenario(scenario)  # 執行正常流量場景
                    con_center_done = threading.Thread(target=self.connect_to_server,
                                                       args=('scenario_done',))
                    con_center_done.start()
                    con_center_done.join()  # 等待執行結束
                # 攻擊開始
                elif parsed_msg['msg'] == "attack_start":
                    self.wifi_reopen_flag = True
                    connection.shutdown(2)
                    connection.close()  # 關閉 socket 連線

        # 必須先關閉 socket 連線裝置才能執行裝置 wifi 相關動作
        if self.wifi_reopen_flag:
            self.controller.disable_wifi()
            self.controller.enable_wifi()
            self.wifi_reopen_flag = False
        return 0

    def run(self):
        start_hour = int(os.environ.get('START_HOUR'))
        start_minute = int(os.environ.get('START_MINUTE'))
        # 時間到開始
        while True:
            if localtime().tm_hour == start_hour and localtime().tm_min == start_minute:
                self.controller.enable_wifi()
                self.logger.logMsg('Init finish !')
                break
        # 接收 center server的指示
        t = threading.Thread(target=self.wait_for_socket_connection)  # 開始監聽
        t.start()
        t.join()
        return


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    deviceName = ""
    ContactNode(deviceName).run()
