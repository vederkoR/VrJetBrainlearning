import random

num_of_attempts = 8
print("H A N G M A N")
print()
list_ = ["python", "java", "swift", "javascript"]
random.shuffle(list_)
word = list_[0]
word_ = "-" * (len(word))
while num_of_attempts != 0:
    print(word_)
    answer = input("Input a letter:")
    if answer in word:
        if answer in word_:
            print("No improvements.")
            num_of_attempts -= 1
        else:
            for i in range(len(word)):
                if word[i] == answer:
                    word_ = word_[:i] + answer + word_[i + 1:]
    else:
        num_of_attempts -= 1
        print("That letter doesn't appear in the word.")
    print()
    if "-" not in word_:
        print(word)
        print("You guessed the word!")
        print("You survived!")
        break
    if num_of_attempts == 0:
        print("You lost!")