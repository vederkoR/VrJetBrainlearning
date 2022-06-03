import collections
import os
import sys
import requests


def file_opener(dir_to, file_in):
    with open(f'{dir_to}/{file_in}', mode='r', encoding='utf-8') as file_:
        print(file_.read())


last_command = ''
command_stack = collections.deque()
args = sys.argv
dir_ = args[1]
try:
    os.mkdir(dir_)
except FileExistsError:
    pass
# write your code here
while True:
    command = input()
    if '.' in command:
        if 'http' not in command:
            command = 'https://' + command
        name = command[8:].split(".")[0]
        if os.access(f'{dir_}/{name}', os.F_OK):
            file_opener(dir_, name)
        else:
            r = requests.get(command)
            with open(f'{dir_}/{name}', mode='w', encoding='utf-8') as file:
                file.write(r.text)
            print(r.text)
        command_stack.append(command)

    elif command == "exit":
        break
    elif command == 'back':
        if len(command_stack) > 1:
            command_stack.pop()
            file_opener(dir_, command_stack[-1])

    else:
        print("Error: Incorrect URL")