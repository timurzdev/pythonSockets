import socket
import sys


class UdpServer:
    def __init__(self, local_ip: str, local_port: int):
        self.local_ip = local_ip
        self.local_port = local_port
        self.buffer_size = 1024
        self.server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.local_ip, self.local_port))

    def start(self):
        try:
            while True:
                bytes_address_pair = self.server_socket.recvfrom(self.buffer_size)
                message = bytes_address_pair[0]
                address = bytes_address_pair[1]
                print(f"Message is {message} and (IP, port) is {address}")
                message = f"{message.decode()}_response".encode()
                self.server_socket.sendto(message, address)
        except KeyboardInterrupt:
            sys.exit()

