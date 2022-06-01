class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money
        self.cups = cups

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def fill(self):
        print("Write how many ml of water you want to add:")
        self.water += int(input())
        print("Write how many ml of milk you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups you want to add:")
        self.cups += int(input())

    def buy(self):
        self.cups -= 1
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        option = int(input())
        if option == 1:
            self.water -= 250
            self.coffee_beans -= 16
            self.money += 4
        elif option == 2:
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.money += 7
        elif option == 3:
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.money += 6

    def info(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.coffee_beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money""")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(money=550, water=400, milk=540, coffee_beans=120, cups=9)
    coffee_machine.info()
    print()
    print("Write action (buy, fill, take):")
    action = input()
    if action == "buy":
        coffee_machine.buy()
    elif action == "take":
        coffee_machine.take()
    elif action == "fill":
        coffee_machine.fill()
    print()
    coffee_machine.info()
