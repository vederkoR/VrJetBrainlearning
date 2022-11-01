import itertools
from collections import Counter

MINIMAL_LENGTH = 100
string_data = ""


def digits_request():
    row_digits = input()
    processed_digits = "".join([i for i in row_digits if i in ("0", "1")])
    global string_data
    string_data += processed_digits


def interface_1():
    global string_data
    while True:
        print("Print a random string containing 0 or 1:\n")
        digits_request()
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


def main():
    interface_1()
    find_occurrences()
    interface_2()


if __name__ == "__main__":
    main()
