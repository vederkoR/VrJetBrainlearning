import itertools
from collections import Counter
from functools import reduce

MINIMAL_LENGTH = 100
string_data = ""


def digits_request(global_str=False):
    raw_digits = input()
    processed_digits = "".join([i for i in raw_digits if i in ("0", "1")])
    if global_str:
        global string_data
        string_data += processed_digits
    else:
        return processed_digits


def interface_1():
    global string_data
    while True:
        print("Print a random string containing 0 or 1:\n")
        digits_request(True)
        if len(string_data) >= MINIMAL_LENGTH:
            print(f"\nFinal data string:\n{string_data}\n")
            break
        print(f"Current data length is {len(string_data)}, {MINIMAL_LENGTH - len(string_data)} symbols left")


def find_occurrences():
    list_all_triads = [string_data[i:i + 3] + " → " + string_data[i + 3] for i in range(len(string_data) - 3)]
    return Counter(list_all_triads)


def interface_2():
    frequencies = find_occurrences()
    for i in map(''.join, itertools.product('01', repeat=3)):
        print(i + ": " + f"{frequencies[i + ' → 0']},{frequencies[i + ' → 1']}")


def first_three_selector():
    all_threes = Counter([string_data[i:i + 3] for i in range(len(string_data) - 3)])
    return reduce(lambda a, b: a if all_threes[a] > all_threes[b] else b, list(all_threes.keys()))


def str_builder(first_3, string, frequencies):
    str_to_return = first_3
    for i in range(3, len(string)):
        digit_to_add = "0" if frequencies.get(string[i - 3:i] + ' → 0', 0) >= frequencies.get(string[i - 3:i] + ' → 1',
                                                                                              0) else '1'
        str_to_return += digit_to_add
    return str_to_return


def guess_work_output(true_str, pred_str):
    correct = 0
    for i in range(3, len(true_str)):
        if true_str[i] == pred_str[i]:
            correct += 1
    return correct


def main():
    interface_1()
    freq = find_occurrences()
    # interface_2()
    print("\nPlease enter a test string containing 0 or 1:\n")
    first_tree = first_three_selector()
    second_request = digits_request(False)
    print("prediction:")
    predicted = str_builder(first_tree, second_request, freq)
    print(predicted)
    print()
    correct = guess_work_output(second_request, predicted)
    print(
        f"Computer guessed right {correct} out of {len(predicted) - 3} symbols ({100 * (correct / (len(predicted) - 3)):.2f} %)")


if __name__ == "__main__":
    main()
