if __name__ == "__main__":
    number_of_pencils = int(input("How many pencils would you like to use:"))
    first_player = input("Who will be the first (John, Jack):")
    second_player = "Jack" if first_player == "John" else "John"
    numeric_flag = 0
    while number_of_pencils > 0:
        print("|" * number_of_pencils)
        current_player = first_player if numeric_flag % 2 == 0 else second_player
        print(f"{current_player}'s turn:")
        pencils_to_take = int(input())
        number_of_pencils -= pencils_to_take
        numeric_flag += 1

