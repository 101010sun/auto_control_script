import socket
import threading

class ComputerControllerServer:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 5050


    def connect_to_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(())