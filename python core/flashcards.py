# Write your code here
import random


def add_card(card_term, card_definition, dictionary):
    dictionary[card_term] = card_definition


def remove_card(card_term, dictionary):
    del dictionary[card_term]


def import_card(path_to_cards, dictionary):
    with open(path_to_cards, "r") as file:
        n = 0
        for line in file:
            if "@" in line:
                line_striped = line.strip()
                card_term, card_definition = line_striped.split("@")
                dictionary[card_term] = card_definition
                n += 1
    return n


def export_card(path_to_cards, dictionary):
    with open(path_to_cards, "w") as file:
        n = 0
        for k, v in dictionary.items():
            file.write(f"{k}@{v}\n")
            n += 1
    return n


def return_card_def(user_answer, term_to_check, dictionary):
    if dictionary[term_to_check] == user_answer:
        print("Correct!")
    elif user_answer in dictionary.values():
        reversed_dict = {value: key for (key, value) in dictionary.items()}
        print(
            f'Wrong. The right answer is "{dictionary[term_to_check]}", but your definition is correct for/'
            f' "{reversed_dict[user_answer]}".')
    else:
        print(f'Wrong. The right answer is "{dictionary[term_to_check]}".')


def return_term(dictionary):
    list_of_terms = list(dictionary.keys())
    random.shuffle(list_of_terms)
    return list_of_terms[0]


def check_term(dictionary):
    term_to_add = input(f"The card:\n")
    while term_to_add in dictionary.keys():
        term_to_add = input(f'The term "{term_to_add}" already exists. Try again:\n')
    return term_to_add


def check_definition(dictionary):
    definition_to_add = input(f"The definition for card:\n")
    while definition_to_add in dictionary.values():
        definition_to_add = input(f'The definition "{definition_to_add}" already exists. Try again:\n')
    return definition_to_add


my_cards = {}
while True:
    user_command = input('Input the action (add, remove, import, export, ask, exit):\n')
    if user_command == "exit":
        print("Bye bye!")
        break
    elif user_command == "add":
        term = check_term(my_cards)
        definition = check_definition(my_cards)
        add_card(term, definition, my_cards)
        print(f'The pair ("{term}":"{definition}") has been added.')
    elif user_command == "remove":
        term_to_remove = input("Which card?\n")
        if term_to_remove in my_cards:
            remove_card(term_to_remove, my_cards)
            print("The card has been removed.")
        else:
            print(f"Can't remove \"{term_to_remove}\": there is no such card.")
    elif user_command == "import":
        path = input("File name:\n")
        try:
            num = import_card(path, my_cards)
        except FileNotFoundError:
            print("File not found.")
        else:
            print(f"{num} cards have been loaded.")
    elif user_command == "export":
        path = input("File name:\n")
        try:
            num = export_card(path, my_cards)
        except FileNotFoundError:
            print("File not found.")
        else:
            print(f"{num} cards have been saved.")
    elif user_command == "ask":
        num = int(input("How many times to ask?\n"))
        for i in range(num):
            card = return_term(my_cards)
            answer = input(f'Print the definition of "{card}":\n')
            return_card_def(answer, card, my_cards)