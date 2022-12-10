import random

OPTIONS = ['scissors', 'rock', 'paper']


def main():
    while True:
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            break
        if user_choice not in OPTIONS:
            print('Invalid input')
            continue
        computer_choice = random.choice(OPTIONS)
        match (user_choice, computer_choice):
            case ('scissors', 'rock') | ('paper', 'scissors') | ('rock', 'paper'):
                print(f"Sorry, but the computer chose {computer_choice}")
            case ('scissors', 'scissors') | ('paper', 'paper') | ('rock', 'rock'):
                print(f"There is a draw ({computer_choice})")
            case ('scissors', 'paper') | ('paper', 'rock') | ('rock', 'scissors'):
                print(f"Well done. The computer chose {computer_choice} and failed")


if __name__ == '__main__':
    main()
