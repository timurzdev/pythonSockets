import socket
import time


class UdpClient:
    def __init__(self, server_ip: str, server_port: int, msg: str, delay: int):
        self.server_address = (server_ip, server_port)
        self.msg_bytes = str.encode(msg)
        self.delay = delay
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.buffer_size = 1024

    def start(self):
        while True:
            time.sleep(self.delay)
            self.client_socket.sendto(self.msg_bytes, self.server_address)
            bytes_address_pair = self.client_socket.recvfrom(self.buffer_size)
            print(f"Received {bytes_address_pair[0]} from {bytes_address_pair[1]}")
