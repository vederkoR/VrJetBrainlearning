# Write your code here
import re

board = '''-------------------
8| _ _ _ _ _ _ _ _ |
7| _ _ _ _ _ _ _ _ |
6| _ _ _ _ _ _ _ _ |
5| _ _ _ _ _ _ _ _ |
4| _ _ _ _ _ _ _ _ |
3| _ _ _ _ _ _ _ _ |
2| _ _ _ _ _ _ _ _ |
1| _ _ _ _ _ _ _ _ |
 -------------------
   1 2 3 4 5 6 7 8'''.format()
position = input("Enter the knight's starting position:")
if re.fullmatch(r"[1-8] [1-8]", position):
    x, y = position.split(" ")
    x, y = int(x), int(y)
    z = 2 * x + (9 - y) * 21
    print(board[:z] + "X" + board[(z+1):])
else:
    print("Invalid dimensions!")
