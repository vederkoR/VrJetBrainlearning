import random

OPTIONS = ['scissors', 'rock', 'paper']
flag_registered = True


def find_or_set_user(user_name):
    with open('rating.txt') as file:
        for row in file:
            if user_name in row:
                return int(row.strip().split(" ")[1])
    global flag_registered
    flag_registered = False
    return 0


def main():
    user_name = input("Enter your name:")
    score = find_or_set_user(user_name)
    original_score = score
    print("Hello,", user_name)
    while True:
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            break
        if user_choice == '!rating':
            print('Your rating:', score)
            break
        if user_choice not in OPTIONS:
            print('Invalid input')
            continue
        computer_choice = random.choice(OPTIONS)
        match (user_choice, computer_choice):
            case ('scissors', 'rock') | ('paper', 'scissors') | ('rock', 'paper'):
                print(f"Sorry, but the computer chose {computer_choice}")
                score += 0
            case ('scissors', 'scissors') | ('paper', 'paper') | ('rock', 'rock'):
                print(f"There is a draw ({computer_choice})")
                score += 50
            case ('scissors', 'paper') | ('paper', 'rock') | ('rock', 'scissors'):
                print(f"Well done. The computer chose {computer_choice} and failed")
                score += 100


if __name__ == '__main__':
    main()
