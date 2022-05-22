# write your code here
list_ = []
with open(input(), mode='r', encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        if len(line) > 79:
            list_.append(i)

for i in list_:
    print(f"Line {i}: S001 Too long")
