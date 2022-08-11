import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("0.0.0.0", 4444))

while True:
            msg = s.recv(1024)

            print(msg.decode("utf-8"))
            time.sleep(.5)
