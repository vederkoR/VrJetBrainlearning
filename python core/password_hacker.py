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
    with open(r"C:\Users\reshv\PycharmProjects\Password Hacker\Password Hacker\task\hacking\passwords.txt", mode="r") \
            as file:
        for line in file:
            word = line.strip()
            it = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word)))
            for x in it:
                admin_socket.send(x.encode('utf8'))
                buffer_size = 1024
                message = admin_socket.recv(buffer_size)
                if message.decode('utf8') == "Connection success!":
                    flag = True
                    print(x)
                    break
            if flag:
                break
