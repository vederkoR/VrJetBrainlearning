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
    num_of_attempts -= 1
    if answer in word:
        for i in range(len(word)):
            if word[i] == answer:
                word_ = word_[:i] + answer + word_[i + 1:]
    else:
        print("That letter doesn't appear in the word.")
    print()
print("Thanks for playing!")
