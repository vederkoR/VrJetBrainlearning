# Write your code here
import re

v = 8
h = 8
board = ""
board_size = input("Enter your board dimensions:")
while True:
    if re.fullmatch(r"\d\d? \d\d?", board_size):
        h, v = board_size.split(" ")
        h, v = int(h), int(v)
        if v < 10:
            board = " " + "-" * ((3 * h + 1) + 2) + "\n"
            for i in range(0, v):
                board += str(v - i) + "|" + " __" * h + ' |\n'
            board += " " + "-" * ((3 * h + 1) + 2) + "\n"
            board += " " * 2
            for j in range(1, h + 1):
                board += "  " + str(j)
        else:
            board = "  " + "-" * ((4 * h + 1) + 2) + "\n"
            for i in range(0, v):
                if v-i > 9:
                    board += str(v - i) + "|" + " ___" * h + ' |\n'
                else:
                    board += " " + str(v - i) + "|" + " ___" * h + ' |\n'
            board += "  " + "-" * ((4 * h + 1) + 2) + "\n"
            board += " " * 3
            for j in range(1, h+1):
                if j < 10:
                    board += "   " + str(j)
                else:
                    board += "  " + str(j)
        break
    else:
        print("Invalid dimensions!")
        board_size = input("Enter your board dimensions:")

position = input("Enter the knight's starting position:")

while True:
    if re.fullmatch(r"\d\d? \d\d?", position):
        x, y = position.split(" ")
        x, y = int(x), int(y)
        if x > h or y > v or x == 0 or y == 0:
            print("Invalid position!")
            position = input("Enter the knight's starting position:")
            continue
        if v < 10:
            z = ((3 * h + 1) + 4) + (v - y) * (h * 3 + 5) + (x - 1) * 3 + 4
            print(board[:(z - 1)] + " X" + board[(z + 1):])
        else:
            z = ((4 * h + 1) + 4) + (v - y) * (h * 4 + 6) + (x - 1) * 4 + 7
            print(board[:(z-2)] + "  X" + board[(z+1):])
        break
    else:
        print("Invalid position!")
        position = input("Enter the knight's starting position:")
