import re


def predictor(num):
    if (num - 1) % 4 == 0 or (num - 1) % 4 == 1:
        return 1
    elif (num - 1) % 4 == 2:
        return 2
    else:
        return 3


if __name__ == "__main__":
    while True:
        number_of_pencils = input("How many pencils would you like to use:")
        if re.fullmatch(r'\d+', number_of_pencils):
            if number_of_pencils == '0':
                print("The number of pencils should be positive")
            else:
                number_of_pencils = int(number_of_pencils)
                break
        else:
            print("The number of pencils should be numeric")
    first_player = input("Who will be the first (John, Jack):")
    while first_player != "John" and first_player != "Jack":
        first_player = input("Choose between John and Jack")
    second_player = "Jack" if first_player == "John" else "John"
    numeric_flag = 0
    while number_of_pencils > 0:
        print("|" * number_of_pencils)
        current_player = first_player if numeric_flag % 2 == 0 else second_player
        if current_player == "Jack":
            print("Jack's turn:")
            number_to_take = predictor(number_of_pencils)
            number_of_pencils -= number_to_take
            print(number_to_take)

        else:
            print("John's turn!")
            pencils_to_take = input()
            while pencils_to_take not in ("1", "2", "3") or (re.fullmatch(r'\d+', pencils_to_take) and
                                                             number_of_pencils < int(pencils_to_take)):
                if pencils_to_take not in ("1", "2", "3"):
                    print("Possible values: '1', '2' or '3'")
                    pencils_to_take = input()
                    continue
                if number_of_pencils < int(pencils_to_take):
                    print("Too many pencils were taken")
                    pencils_to_take = input()
            pencils_to_take = int(pencils_to_take)
            number_of_pencils -= pencils_to_take
        numeric_flag += 1
        if number_of_pencils == 0:
            current_player = first_player if numeric_flag % 2 == 0 else second_player
            print(f"{current_player} won!")
            break

