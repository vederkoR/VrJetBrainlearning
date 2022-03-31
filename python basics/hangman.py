import random

num_of_attempts = 8
print("H A N G M A N")
print()
list_ = ["python", "java", "swift", "javascript"]
list__ = []
random.shuffle(list_)
word = list_[0]
word_ = "-" * (len(word))
while num_of_attempts != 0:
    print(word_)
    answer = input("Input a letter:")
    if len(answer) == 1 and ord(answer) not in range(ord('a'), ord('z') + 1):
        print("Please, enter a lowercase letter from the English alphabet.")
        continue
    if len(answer) != 1:
        print("Please, input a single letter.")
        continue
    if answer in list__:
        print("You've already guessed this letter.")
        continue
    list__.append(answer)
    if answer in word:
        for i in range(len(word)):
            if word[i] == answer:
                word_ = word_[:i] + answer + word_[i + 1:]
    else:
        num_of_attempts -= 1
        print("That letter doesn't appear in the word.")
    print()
    if "-" not in word_:
        print(f"You guessed the word {word}!")
        print("You survived!")
        break
    if num_of_attempts == 0:
        print("You lost!")
