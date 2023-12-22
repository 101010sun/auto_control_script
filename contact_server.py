from cellphone import SamsungS20FEController
from cellphone import OppoReno7Controller
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
        self.asus_port = int(os.environ.get("ASUS_PORT"))

        self.msi_host = os.environ.get("MSI_HOST")
        self.msi_port = int(os.environ.get("MSI_PORT"))
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
        start_hour = int(os.environ.get('START_HOUR'))
        start_minute = int(os.environ.get('START_MINUTE'))
        # 時間到開始
        while True:
            if localtime().tm_hour == start_hour and localtime().tm_min == start_minute:
                self.logger.logMsg('Init finish !')
            elif localtime().tm_hour == start_hour and localtime().tm_min == (start_minute + 2):
                self.logger.logMsg('Call device do scenario !')
                break

        # 宣告手機裝置的 controller
        samsung_adb_name = os.environ.get("SAMSUNG_DEVICE_NAME")
        oppo_adb_name = os.environ.get("OPPO_DEVICE_NAME")
        
        samsungS20FE = SamsungS20FEController(samsung_adb_name)
        oppoReno7 = OppoReno7Controller(oppo_adb_name)

        # 依裝置順序執行正常流量場景
        self.logger.logMsg('Choose scenario !')
        # samsung cellphone
        scenario_value = self.get_random_scenario()
        act_samsung_scenario = threading.Thread(target=samsungS20FE.process_scenario,
                                                args=(scenario_value,))
        act_samsung_scenario.start()
        # oppo cellphone
        scenario_value = self.get_random_scenario()
        act_oppo_scenario = threading.Thread(target=oppoReno7.process_scenario,
                                             args=(scenario_value,))
        act_oppo_scenario.start()
        # iphone cellphone (manual)
        scenario_value = self.get_random_scenario()
        self.logger.logMsg(f"IPhone do scenario {scenario_value}")
        # acer laptop
        scenario_value = self.get_random_scenario()
        conn_acer_scenario = threading.Thread(target=self.connect_to_client,
                                              args=(self.acer_host, self.acer_port, 'normal_flow', scenario_value,))
        conn_acer_scenario.start()
        # asus laptop
        scenario_value = self.get_random_scenario()
        conn_asus_scenario = threading.Thread(target=self.connect_to_client,
                                              args=(self.asus_host, self.asus_port, 'normal_flow', scenario_value,))
        conn_asus_scenario.start()
        # msi laptop
        scenario_value = self.get_random_scenario()
        conn_msi_scenario = threading.Thread(target=self.connect_to_client,
                                             args=(self.msi_host, self.msi_port, 'normal_flow', scenario_value,))
        conn_msi_scenario.start()

        # 等待場景都執行完成
        t = threading.Thread(target=self.wait_for_socket_connection)  # 開始監聽
        t.start()
        t.join()
        conn_acer_scenario.join()
        conn_asus_scenario.join()
        conn_msi_scenario.join()
        act_samsung_scenario.join()
        act_oppo_scenario.join()

        # 攻擊階段開始
        # 通知 attacker

        # 裝置依序 reable wifi
        samsungS20FE.disable_wifi()
        samsungS20FE.enable_wifi()

        oppoReno7.disable_wifi()
        oppoReno7.enable_wifi()

        self.logger.logMsg(f"IPhone attack start ! (disable & enable wifi)")

        conn_acer_attack = threading.Thread(target=self.connect_to_client,
                                            args=(self.acer_host, self.acer_port, 'attack_start',))
        conn_acer_attack.start()

        conn_asus_attack = threading.Thread(target=self.connect_to_client,
                                            args=(self.asus_host, self.asus_port, 'attack_start',))
        conn_asus_attack.start()

        conn_msi_attack = threading.Thread(target=self.connect_to_client,
                                           args=(self.msi_host, self.msi_port, 'attack_start',))
        conn_msi_attack.start()
        return


if __name__ == "__main__":
    logger = Logger('WPA3DataSet', 'main')
    ContactServer().run()
