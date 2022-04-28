import itertools
import socket
import string
import sys

symbols = list(string.ascii_lowercase + string.digits)
args = sys.argv
ip_address = args[1]
port = int(args[2])
flag = False
with socket.socket() as admin_socket:
    admin_socket.connect((ip_address, port))
    for i in range(1, 10):
        for x in itertools.product(symbols, repeat=i):
            tried = "".join(x)
            admin_socket.send(tried.encode())
            buffer_size = 1024
            message = admin_socket.recv(buffer_size)
            if message.decode() == "Connection success!":
                flag = True
                print(tried)
                break
        if flag:
            break
