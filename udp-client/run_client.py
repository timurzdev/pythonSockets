import sys
from udpClient import UdpClient

if __name__ == "__main__":
    args = sys.argv
    client = UdpClient(args[1], int(args[2]), args[3], int(args[4]))
    client.start()