import random

print("H A N G M A N")

list_ = ["python", "java", "swift", "javascript"]
random.shuffle(list_)
word = list_[0]
answer = input(f"Guess the word {word[0 : 3]}" + '-'*(len(word)-3) + ":")
if answer == word:
    print("You survived!")
else:
    print("You lost!")
