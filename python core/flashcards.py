# Write your code here
cards = dict()
num = int(input("Input the number of cards:\n"))
for i in range(num):
    term =input(f"The term for card #{i + 1}:\n")
    definition = input(f"The definition for card #{i + 1}:\n")
    cards[term] = definition
for chosen in cards.keys():
    answer = input(f'Print the definition of "{chosen}":\n')
    if cards[chosen] == answer:
        print("Correct!")
    else:
        print(f'Wrong. The right answer is "{cards[chosen]}".')