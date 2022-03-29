result_not_finished = "Game not finished"
result_draw = "Draw"
result_x_win = "X wins"
result_o_win = "O wins"
result_impossible = "Impossible"

players_input = input("Enter cells:")
tmp = players_input
print("---------")
print("| {} {} {} |".format(players_input[0], players_input[1], players_input[2]))
print("| {} {} {} |".format(players_input[3], players_input[4], players_input[5]))
print("| {} {} {} |".format(players_input[6], players_input[7], players_input[8]))
print("---------")

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
