import random


def add_card(card_term, card_definition, dictionary):
    dictionary[card_term] = [card_definition, 0]


def remove_card(card_term, dictionary):
    del dictionary[card_term]


def import_card(path_to_cards, dictionary):
    with open(path_to_cards, "r") as file:
        n = 0
        for line in file:
            if "@" in line:
                line_striped = line.strip()
                card_term, card_definition, wrong_answers = line_striped.split("@")
                dictionary[card_term] = [card_definition, int(wrong_answers)]
                n += 1
    return n


def export_card(path_to_cards, dictionary):
    with open(path_to_cards, "w") as file:
        n = 0
        for k, v in dictionary.items():
            file.write(f"{k}@{v[0]}@{str(v[1])}\n")
            n += 1
    return n


def return_card_def(user_answer, term_to_check, dictionary):
    dictionary_to_return = dictionary
    if dictionary_to_return[term_to_check] == user_answer:
        print(add_to_log("Correct!"))
    elif user_answer in [x[0] for x in dictionary_to_return.values()]:
        reversed_dict = {value[0]: key for (key, value) in dictionary_to_return.items()}
        print(add_to_log(
            f'Wrong. The right answer is "{dictionary_to_return[term_to_check][0]}", but your definition is correct for'
            f' "{reversed_dict[user_answer]}".'))
        dictionary_to_return[term_to_check][1] = dictionary_to_return[term_to_check][1] + 1
    else:
        print(add_to_log(f'Wrong. The right answer is "{dictionary_to_return[term_to_check][0]}".'))
        dictionary_to_return[term_to_check][1] = dictionary_to_return[term_to_check][1] + 1


def return_term(dictionary):
    list_of_terms = list(dictionary.keys())
    random.shuffle(list_of_terms)
    return list_of_terms[0]


def check_term(dictionary):
    term_to_add = input(add_to_log(f"The card:\n"))
    add_to_log(term_to_add)
    while term_to_add in dictionary.keys():
        term_to_add = input(add_to_log(f'The term "{term_to_add}" already exists. Try again:\n'))
        add_to_log(term_to_add)
    return term_to_add


def check_definition(dictionary):
    definition_to_add = input(add_to_log(f"The definition for card:\n"))
    add_to_log(definition_to_add)
    while definition_to_add in [x[0] for x in dictionary.values()]:
        definition_to_add = input(add_to_log(f'The definition "{definition_to_add}" already exists. Try again:\n'))
        add_to_log(definition_to_add)
    return definition_to_add


def add_to_log(message):
    global log
    stripped_message = message.strip()
    log += stripped_message + "\n"
    return message


def save_log(path_to_log):
    global log
    with open(path_to_log, "w") as file:
        file.write(log)
        print(add_to_log("The log has been saved."))


def find_hardest_card(dictionary):
    list_of_values = [x[1] for x in dictionary.values()]
    if not [x for x in list_of_values if x > 0]:
        return dict()
    else:
        return {key: value for (key, value) in dictionary.items() if value[1] == max(list_of_values)}


my_cards = {}
log = ""
while True:
    user_command = input(
        add_to_log('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n'))
    add_to_log(user_command)
    if user_command == "exit":
        print(add_to_log("Bye bye!"))
        break
    elif user_command == "add":
        term = check_term(my_cards)
        definition = check_definition(my_cards)
        add_card(term, definition, my_cards)
        print(add_to_log(f'The pair ("{term}":"{definition}") has been added.'))
    elif user_command == "remove":
        term_to_remove = input(add_to_log("Which card?\n"))
        add_to_log(term_to_remove)
        if term_to_remove in my_cards:
            remove_card(term_to_remove, my_cards)
            print(add_to_log("The card has been removed."))
        else:
            print(add_to_log(f"Can't remove \"{term_to_remove}\": there is no such card."))
    elif user_command == "import":
        path = input(add_to_log("File name:\n"))
        add_to_log(path)
        try:
            num = import_card(path, my_cards)
        except FileNotFoundError:
            print(add_to_log("File not found."))
        else:
            print(add_to_log(f"{num} cards have been loaded."))
    elif user_command == "export":
        path = input(add_to_log("File name:\n"))
        add_to_log(path)
        try:
            num = export_card(path, my_cards)
        except FileNotFoundError:
            print(add_to_log("File not found."))
        else:
            print(add_to_log(f"{num} cards have been saved."))
    elif user_command == "ask":
        num = int(input(add_to_log("How many times to ask?\n")))
        add_to_log(str(num))
        for i in range(num):
            card = return_term(my_cards)
            answer = input(add_to_log(f'Print the definition of "{card}":\n'))
            add_to_log(answer)
            return_card_def(answer, card, my_cards)
    elif user_command == "log":
        print(log)
        log_file = input(add_to_log("File name:"))
        add_to_log(log_file)
        save_log(log_file)
    elif user_command == "hardest card":
        hardest = find_hardest_card(my_cards)
        if len(hardest) == 0:
            print(add_to_log("There are no cards with errors."))
        elif len(hardest) == 1:
            key_1 = list(hardest.keys())[0]
            print(add_to_log(f'The hardest card is "{key_1}". You have {hardest[key_1][1]} errors answering it'))
        else:
            terms = []
            for key_loc in hardest.keys():
                terms.append(f'"{key_loc}"')
            terms = ", ".join(terms)
            print(add_to_log(f'The hardest cards are {terms}'))
    elif user_command == "reset stats":
        for card in my_cards.keys():
            my_cards[card][1] = 0
        print(add_to_log("Card statistics have been reset."))
