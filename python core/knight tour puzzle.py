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
                if v - i > 9:
                    board += str(v - i) + "|" + " ___" * h + ' |\n'
                else:
                    board += " " + str(v - i) + "|" + " ___" * h + ' |\n'
            board += "  " + "-" * ((4 * h + 1) + 2) + "\n"
            board += " " * 3
            for j in range(1, h + 1):
                if j < 10:
                    board += "   " + str(j)
                else:
                    board += "  " + str(j)
        break
    else:
        print("Invalid dimensions!")
        board_size = input("Enter your board dimensions:")

position = input("Enter the knight's starting position:")


def check_pos(hor, ver, x_pos, y_pos):
    if ver < 10:
        z = ((3 * hor + 1) + 4) + (ver - y_pos) * (hor * 3 + 5) + (x_pos - 1) * 3 + 4
    else:
        z = ((4 * hor + 1) + 4) + (ver - y_pos) * (hor * 4 + 6) + (x_pos - 1) * 4 + 7
    return z


def options_checker(hor, ver, x_pos, y_pos):
    options = []
    if x_pos + 2 <= hor and y_pos + 1 <= ver:
        options.append((x_pos + 2, y_pos + 1))
    if x_pos + 2 <= hor and y_pos - 1 > 0:
        options.append((x_pos + 2, y_pos - 1))
    if x_pos - 2 > 0 and y_pos + 1 <= ver:
        options.append((x_pos - 2, y_pos + 1))
    if x_pos - 2 > 0 and y_pos - 1 > 0:
        options.append((x_pos - 2, y_pos - 1))
    if x_pos + 1 <= hor and y_pos + 2 <= ver:
        options.append((x_pos + 1, y_pos + 2))
    if x_pos + 1 <= hor and y_pos - 2 > 0:
        options.append((x_pos + 1, y_pos - 2))
    if x_pos - 1 > 0 and y_pos + 2 <= ver:
        options.append((x_pos - 1, y_pos + 2))
    if x_pos - 1 > 0 and y_pos - 2 > 0:
        options.append((x_pos - 1, y_pos - 2))
    return options


def board_update(board_init, z_pos, sym, vr):
    if vr < 10:
        return board_init[:(z_pos - 1)] + " " + sym + board_init[(z_pos + 1):]
    else:
        return board_init[:(z_pos - 2)] + "  " + sym + board_init[(z_pos + 1):]


def place_pos(hor, ver, x_pos, y_pos, board_orig):
    z_for_x = check_pos(hor, ver, x_pos, y_pos)
    board_ret = board_update(board_orig, z_for_x, "X", ver)
    opts = options_checker(hor, ver, x_pos, y_pos)
    for opt in opts:
        z_for_o = check_pos(hor, ver, opt[0], opt[1])
        num = len(options_checker(hor, ver, opt[0], opt[1])) - 1
        board_ret = board_update(board_ret, z_for_o, str(num), ver)
    return board_ret


while True:
    if re.fullmatch(r"\d\d? \d\d?", position):
        x, y = position.split(" ")
        x, y = int(x), int(y)
        if x > h or y > v or x == 0 or y == 0:
            print("Invalid position!")
            position = input("Enter the knight's starting position:")
            continue
        print(place_pos(h, v, x, y, board))
        break
    else:
        print("Invalid position!")
        position = input("Enter the knight's starting position:")