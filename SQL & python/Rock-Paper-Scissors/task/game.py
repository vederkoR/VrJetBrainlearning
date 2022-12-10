import random


def find_or_set_user(user_name):
    try:
        with open('rating.txt') as file:
            for row in file:
                if user_name in row:
                    return int(row.strip().split(" ")[1])
    except FileNotFoundError:
        pass
    return 0


def main():
    user_name = input("Enter your name:")
    score = find_or_set_user(user_name)
    print("Hello,", user_name)
    options = input()
    if not options:
        options = 'scissors,rock,paper'
    options = options.split(",")
    print("Okay, let's start")

    while True:
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            break
        if user_choice == '!rating':
            print('Your rating:', score)
            break
        if user_choice not in options:
            print('Invalid input')
            continue
        computer_choice = random.choice(options)
        index_of_user_chose = options.index(user_choice)
        list_for_decision = options[index_of_user_chose + 1:] + options[:index_of_user_chose]
        if computer_choice == user_choice:
            print(f"There is a draw ({computer_choice})")
            score += 50
        elif list_for_decision.index(computer_choice) < len(list_for_decision) / 2:
            print(f"Sorry, but the computer chose {computer_choice}")
            score += 0
        else:
            print(f"Well done. The computer chose {computer_choice} and failed")
            score += 100


if __name__ == '__main__':
    main()
