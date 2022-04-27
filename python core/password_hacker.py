import socket
import sys

args = sys.argv
ip_address = args[1]
port = int(args[2])
password = args[3]
with socket.socket() as admin_socket:
    admin_socket.connect((ip_address, port))
    admin_socket.send(password.encode())

    buffer_size = 1024
    message = admin_socket.recv(buffer_size)
    print(message.decode())

