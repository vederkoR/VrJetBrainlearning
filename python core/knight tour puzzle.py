# Write your code here
import re

v = 8
h = 8
board = ""
board_size = input("Enter your board dimensions:")
forbidden_positions = []
available_moves = []
current_position = (0, 0)
while True:
    if re.fullmatch(r"\d\d? \d\d?", board_size):
        h, v = board_size.split(" ")
        h, v = int(h), int(v)
        if h == 0 or v == 0:
            print("Invalid dimensions!")
            board_size = input("Enter your board dimensions:")
            continue
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
    if x_pos + 2 <= hor and y_pos + 1 <= ver and (x_pos + 2, y_pos + 1) not in forbidden_positions:
        options.append((x_pos + 2, y_pos + 1))
    if x_pos + 2 <= hor and y_pos - 1 > 0 and (x_pos + 2, y_pos - 1) not in forbidden_positions:
        options.append((x_pos + 2, y_pos - 1))
    if x_pos - 2 > 0 and y_pos + 1 <= ver and (x_pos - 2, y_pos + 1) not in forbidden_positions:
        options.append((x_pos - 2, y_pos + 1))
    if x_pos - 2 > 0 and y_pos - 1 > 0 and (x_pos - 2, y_pos - 1) not in forbidden_positions:
        options.append((x_pos - 2, y_pos - 1))
    if x_pos + 1 <= hor and y_pos + 2 <= ver and (x_pos + 1, y_pos + 2) not in forbidden_positions:
        options.append((x_pos + 1, y_pos + 2))
    if x_pos + 1 <= hor and y_pos - 2 > 0 and (x_pos + 1, y_pos - 2) not in forbidden_positions:
        options.append((x_pos + 1, y_pos - 2))
    if x_pos - 1 > 0 and y_pos + 2 <= ver and (x_pos - 1, y_pos + 2) not in forbidden_positions:
        options.append((x_pos - 1, y_pos + 2))
    if x_pos - 1 > 0 and y_pos - 2 > 0 and (x_pos - 1, y_pos - 2) not in forbidden_positions:
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
        num = len(options_checker(hor, ver, opt[0], opt[1]))
        board_ret = board_update(board_ret, z_for_o, str(num), ver)
    for pos in forbidden_positions:
        z_for_star = check_pos(hor, ver, pos[0], pos[1])
        board_ret = board_update(board_ret, z_for_star, '*', ver)
    global available_moves
    available_moves = opts
    z_for_x = check_pos(hor, ver, x_pos, y_pos)
    board_ret = board_update(board_ret, z_for_x, "X", ver)
    return board_ret


while True:
    if re.fullmatch(r"\d\d? \d\d?", position):
        x, y = position.split(" ")
        x, y = int(x), int(y)
        if x > h or y > v or x == 0 or y == 0:
            print("Invalid position!")
            position = input("Enter the knight's starting position:")
            continue
        forbidden_positions.append((x, y))
        current_position = (x, y)
        print(place_pos(h, v, x, y, board))
        break
    else:
        print("Invalid position!")
        position = input("Enter the knight's starting position:")
flag_1 = 'off'

while True:
    if h * v == len(forbidden_positions):
        print("What a great tour! Congratulations!")
        break
    elif not available_moves:
        print("No more possible moves!")
        print("Your knight visited {} squares!".format(len(forbidden_positions)))
        break
    else:
        if flag_1 == 'off':
            next_position = input("Enter your next move:")
        else:
            next_position = input("Invalid move! Enter your next move:")
        if re.fullmatch(r"\d\d? \d\d?", next_position):
            x, y = next_position.split(" ")
            x, y = int(x), int(y)
            if (x > h or y > v or x == 0 or y == 0) or (x, y) not in available_moves:
                flag_1 = 'on'
                continue
            else:
                forbidden_positions.append((x, y))
                current_position = (x, y)
                print(place_pos(h, v, x, y, board))
