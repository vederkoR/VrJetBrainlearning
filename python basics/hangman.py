import random
print("H A N G M A N")
won_score = 0
lost_score = 0


def play():
    num_of_attempts = 8
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
            global won_score
            won_score += 1
            break
        if num_of_attempts == 0:
            print("You lost!")
            global lost_score
            lost_score += 1


def results():
    print(f"You won: {won_score} times.")
    print(f"You lost: {lost_score} times.")


while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if choice == "exit":
        break
    if choice == "play":
        play()
    if choice == "results":
        results()