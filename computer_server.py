import socket
import threading

class ComputerControllerServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 5050


    def connect_to_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(())
        return 0


    # 監聽 func.
    def wait_for_socket_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.socket_host, self.socket_port))
            s.listen()
            while True:
                conn, address = s.accept()
                client_handler = threading.Thread(target=self.receive_socket_message, args=(s, conn, address)) # 處理收到的請求
                client_handler.start()


    # 處理請求 func.
    def receive_socket_message(self, s, connection ,address):
        with connection:
            return 0
        
        