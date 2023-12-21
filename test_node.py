from base import Logger
from dotenv import load_dotenv
from time import localtime
import socket
import threading
import os
import pickle

# 載入環境變數
load_dotenv()


class ContactNode:
    def __init__(self, deviceName: str):
        self.logger = Logger('WPA3Dataset', 'contact_node')
        self.server_host = os.environ.get("CENTER_HOST")
        self.server_port = os.environ.get("CENTER_PORT")
        self.device = deviceName

        if deviceName == 'AcerT9300':
            self.host = os.environ.get("ACER_HOST")
            self.port = os.environ.get("ACER_PORT")

        elif deviceName == 'ASUSA550v':
            self.host = os.environ.get("ASUS_HOST")
            self.port = os.environ.get("ASUS_PORT")

        elif deviceName == 'MSIM16':
            self.host = os.environ.get("MSI_HOST")
            self.port = os.environ.get("MSI_PORT")

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
                    print(f"{parsed_msg['msg']} {scenario}")
                    con_center_done = threading.Thread(target=self.connect_to_server,
                                                       args=('scenario_done',))
                    con_center_done.start()
                    con_center_done.join()  # 等待執行結束
                # 攻擊開始
                elif parsed_msg['msg'] == "attack_start":
                    self.wifi_reopen_flag = True
                    print(f"{parsed_msg['msg']} {self.wifi_reopen_flag}")
                    connection.shutdown(2)
                    connection.close()  # 關閉 socket 連線

        return 0

    def run(self):
        # 接收 center server的指示
        t = threading.Thread(target=self.wait_for_socket_connection)  # 開始監聽
        t.start()
        t.join()
        return


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    deviceName = ""
    ContactNode(deviceName).run()
