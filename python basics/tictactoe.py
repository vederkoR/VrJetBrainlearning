import re

result_not_finished = "Game not finished"
result_draw = "Draw"
result_x_win = "X wins"
result_o_win = "O wins"
result_impossible = "Impossible"
max_field = 3

players_input = input("Enter cells:")
tmp = players_input


def draw_board():
    print("---------")
    print("| {} {} {} |".format(tmp[0], tmp[1], tmp[2]))
    print("| {} {} {} |".format(tmp[3], tmp[4], tmp[5]))
    print("| {} {} {} |".format(tmp[6], tmp[7], tmp[8]))
    print("---------")


draw_board()
while True:
    new_pos = input("Enter the coordinates: ")
    match = re.match(r'\d+\s\d+', new_pos)
    if match is None:
        print("You should enter numbers!")
        continue
    elif int(new_pos.split(" ")[0]) > max_field or int(new_pos.split(" ")[1]) > max_field:
        print("Coordinates should be from 1 to 3!")
        continue
    elif tmp[(int(new_pos[0]) - 1) * 3 + (int(new_pos[2]) - 1)] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    else:
        pos_ = (int(new_pos[0]) - 1) * 3 + (int(new_pos[2]) - 1)
        tmp = tmp[:pos_] + 'X' + tmp[(pos_ + 1):]
        draw_board()
        break

x_ = tmp[0] == tmp[1] == tmp[2] == "X" or tmp[3] == tmp[4] == tmp[5] == "X" or tmp[6] == tmp[7] == tmp[8] == "X" or tmp[
    0] == tmp[3] == tmp[6] == "X" or tmp[1] == tmp[4] == tmp[7] == "X" or tmp[2] == tmp[5] == tmp[8] == "X" or tmp[0] == \
     tmp[4] == tmp[8] == "X" or tmp[2] == tmp[4] == tmp[6] == "X"
o_ = tmp[0] == tmp[1] == tmp[2] == "O" or tmp[3] == tmp[4] == tmp[5] == "O" or tmp[6] == tmp[7] == tmp[8] == "O" or tmp[
    0] == tmp[3] == tmp[6] == "O" or tmp[1] == tmp[4] == tmp[7] == "O" or tmp[2] == tmp[5] == tmp[8] == "O" or tmp[0] == \
     tmp[4] == tmp[8] == "O" or tmp[2] == tmp[4] == tmp[6] == "O"
if abs(players_input.count("X") - players_input.count("O")) > 1 or (x_ and o_):
    print(result_impossible)

elif x_:
    print(result_x_win)
elif o_:
    print(result_o_win)
elif "_" not in players_input:
    print(result_draw)
else:
    print(result_not_finished)
