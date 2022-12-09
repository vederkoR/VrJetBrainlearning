loser_mapping = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}


def main():
    choice = input()
    print(f"Sorry, but the computer chose {loser_mapping[choice]}")


if __name__ == '__main__':
    main()
