from udpServer import UdpServer
import sys


if __name__ == '__main__':
    args = sys.argv
    server = UdpServer(args[1], int(args[2]))
    server.listen()
