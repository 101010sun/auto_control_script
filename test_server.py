from base import Logger
from dotenv import load_dotenv
from time import localtime
import socket
import threading
import os
import pickle
import random

# 載入環境變數
load_dotenv()


class ContactServer:
    # server接有線連接不斷線
    def __init__(self):
        self.logger = Logger('WPA3Dataset', 'contact_server')
        self.host = os.environ.get("CENTER_HOST")
        self.port = int(os.environ.get("CENTER_PORT"))

        self.acer_host = os.environ.get("ACER_HOST")
        self.acer_port = int(os.environ.get("ACER_PORT"))

        self.asus_host = os.environ.get("ASUS_HOST")
        self.asus_port = os.environ.get("ASUS_PORT")

        self.msi_host = os.environ.get("MSI_HOST")
        self.msi_port = os.environ.get("MSI_PORT")
        self.done_device_counter = 0
        self.scenario_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 總共9個場景

    def connect_to_client(self, clientHost: str, clientPort: int, msg: str, scenario: int = 0):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((clientHost, clientPort))  # 連接
            message = {'msg': msg}
            if scenario != 0:
                message['scenario'] = scenario

            s.send(pickle.dumps(message))

            s.shutdown(2)  # 中斷連接
            s.close()  # 關閉
        return

    # 監聽 func.
    def wait_for_socket_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            while True:
                conn, address = s.accept()
                client_handler = threading.Thread(
                    target=self.receive_socket_message, args=(s, conn, address))  # 處理收到的請求
                client_handler.start()
                if not client_handler.is_alive():
                    client_handler.join()
                    break
            s.shutdown(2)
            s.close()

    # 處理請求 func.
    def receive_socket_message(self, s: socket.socket, connection: socket.socket, address):
        with connection:
            message = connection.recv(1024)  # 接收 msg
            try:
                parsed_msg = pickle.loads(message)  # 轉譯 msg
            except Exception:
                self.logger.logMsg(f"{message} cannot be parsed")
            self.logger.logMsg(f"Received: {parsed_msg}")

            if message:
                if parsed_msg['msg'] == "scenario_done":
                    self.done_device_counter += 1
                    if self.done_device_counter >= 3:
                        connection.shutdown(2)
                        connection.close()  # 關閉 socket 連線

    def get_random_scenario(self):
        random_index = random.randint(0, len(self.scenario_list)-1)
        value = self.scenario_list[random_index]
        self.scenario_list.remove(value)
        return value

    def run(self):

        # 依裝置順序執行正常流量場景
        self.logger.logMsg('Choose scenario !')

        # acer laptop
        scenario_value = self.get_random_scenario()
        conn_acer_scenario = threading.Thread(target=self.connect_to_client,
                                              args=(self.acer_host, self.acer_port, 'normal_flow', scenario_value,))
        conn_acer_scenario.start()

        # 等待場景都執行完成
        t = threading.Thread(target=self.wait_for_socket_connection)  # 開始監聽
        t.start()
        t.join()
        conn_acer_scenario.join()

        # 攻擊階段開始
        # 通知 attacker

        conn_acer_attack = threading.Thread(target=self.connect_to_client,
                                            args=(self.acer_host, self.acer_port, 'attack_start',))
        conn_acer_attack.start()
        return


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    ContactServer().run()
