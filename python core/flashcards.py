cards = dict()
back_cards = dict()
num = int(input("Input the number of cards:\n"))
for i in range(num):
    term = input(f"The term for card #{i + 1}:\n")
    while term in cards.keys():
        term = input(f'The term "{term}" already exists. Try again:\n')
    definition = input(f"The definition for card #{i + 1}:\n")
    while definition in back_cards.keys():
        definition = input(f'The definition "{definition}" already exists. Try again:\n')
    cards[term] = definition
    back_cards[definition] = term
for chosen in cards.keys():
    answer = input(f'Print the definition of "{chosen}":\n')
    if cards[chosen] == answer:
        print("Correct!")
    elif answer in back_cards.keys():
        print(
            f'Wrong. The right answer is "{cards[chosen]}", but your definition is correct for "{back_cards[answer]}".')
    else:
        print(f'Wrong. The right answer is "{cards[chosen]}".')