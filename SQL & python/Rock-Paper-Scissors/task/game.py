import random

loser_mapping = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}


def main():
    user_choice = input()
    computer_choice = random.choice(['scissors', 'rock', 'paper'])
    match (user_choice, computer_choice):
        case ('scissors', 'rock') | ('paper', 'scissors') | ('rock', 'paper'):
            print(f"Sorry, but the computer chose {computer_choice}")
        case ('scissors', 'scissors') | ('paper', 'paper') | ('rock', 'rock'):
            print(f"There is a draw ({computer_choice})")
        case ('scissors', 'paper') | ('paper', 'rock') | ('rock', 'scissors'):
            print(f"Well done. The computer chose {computer_choice} and failed")


if __name__ == '__main__':
    main()
