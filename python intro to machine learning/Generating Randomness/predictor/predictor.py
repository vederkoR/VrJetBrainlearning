MINIMAL_LENGTH = 100
string_data = ""


def digits_request():
    row_digits = input()
    processed_digits = "".join([i for i in row_digits if i in ("0", "1")])
    global string_data
    string_data += processed_digits


def interface():
    global string_data
    while True:
        print("Print a random string containing 0 or 1:\n")
        digits_request()
        if len(string_data) >= MINIMAL_LENGTH:
            print(f"\nFinal data string:\n{string_data}")
            break
        print(f"Current data length is {len(string_data)}, {MINIMAL_LENGTH - len(string_data)} symbols left")


def main():
    interface()


if __name__ == "__main__":
    main()
