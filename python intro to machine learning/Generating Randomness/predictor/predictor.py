import itertools
from collections import Counter
from functools import reduce


class Game:
    MINIMAL_LENGTH = 100

    def __init__(self):
        self.string_data = ""
        self.frequencies = None
        self.first_three = None
        self.balance = 1000

    def digits_request(self, global_str=False):
        raw_digits = input()
        if raw_digits == "enough":
            return "q"
        processed_digits = "".join([i for i in raw_digits if i in ("0", "1")])
        if global_str:
            self.string_data += processed_digits
        else:
            return processed_digits

    def interface_1(self):
        while True:
            print("Print a random string containing 0 or 1:\n")
            self.digits_request(True)
            if len(self.string_data) >= Game.MINIMAL_LENGTH:
                print(f"\nFinal data string:\n{self.string_data}\n")
                break
            print(f"Current data length is {len(self.string_data)}, "
                  f"{Game.MINIMAL_LENGTH - len(self.string_data)} symbols left")

    def find_occurrences(self):
        list_all_triads = [self.string_data[i:i + 3] + " → " + self.string_data[i + 3] for i in
                           range(len(self.string_data) - 3)]
        self.frequencies = Counter(list_all_triads)

    def interface_2(self):
        for i in map(''.join, itertools.product('01', repeat=3)):
            print(i + ": " + f"{self.frequencies[i + ' → 0']},{self.frequencies[i + ' → 1']}")

    def first_three_selector(self):
        all_threes = Counter([self.string_data[i:i + 3] for i in range(len(self.string_data) - 3)])
        self.first_three = reduce(lambda a, b: a if all_threes[a] > all_threes[b] else b, list(all_threes.keys()))

    @staticmethod
    def str_builder(first_3, string, frequencies):
        str_to_return = first_3
        for i in range(3, len(string)):
            digit_to_add = "0" if frequencies.get(string[i - 3:i] + ' → 0', 0) >= frequencies.get(
                string[i - 3:i] + ' → 1',
                0) else '1'
            str_to_return += digit_to_add
        return str_to_return

    @staticmethod
    def guess_work_output(true_str, pred_str):
        correct = 0
        for i in range(3, len(true_str)):
            if true_str[i] == pred_str[i]:
                correct += 1
        return correct


def main():
    print("Please give AI some data to learn...")
    print("The current data length is 0, 100 symbols left")
    game = Game()
    game.interface_1()
    game.find_occurrences()
    # interface_2()
    print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")
    while True:
        print("\nPrint a random string containing 0 or 1:")
        second_request = game.digits_request(False)
        if second_request == "q":
            print("Game over!")
            break
        elif len(second_request) > 3:
            print("prediction:")
            game.first_three_selector()
            predicted = game.str_builder(game.first_three, second_request, game.frequencies)
            print(predicted)
            print()
            correct = game.guess_work_output(second_request, predicted)
            percentage = correct / (len(predicted) - 3)
            print(
                f"Computer guessed right {correct} out of {len(predicted) - 3} symbols ({100 * percentage:.2f} %)")
            game.balance -= correct
            game.balance += (len(predicted) - 3) - correct
            print(f"Your balance is now ${game.balance}")


if __name__ == "__main__":
    main()
