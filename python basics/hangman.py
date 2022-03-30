import random

print("H A N G M A N")

list_ = ["python", "java", "swift", "javascript"]
random.shuffle(list_)

answer = input("Guess the word:")
if answer == list_[0]:
    print("You survived!")
else:
    print("You lost!")
