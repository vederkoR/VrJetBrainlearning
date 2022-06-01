class Coffee:
    def __init__(self, water=0, milk=0, coffee_beans=0, money=0):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money


class CoffeeMachine:
    espresso = Coffee(water=250, coffee_beans=16, money=4)
    latte = Coffee(water=350, coffee_beans=20, money=7, milk=75)
    cappuccino = Coffee(water=200, coffee_beans=12, money=6, milk=100)
    options = {"1": espresso, "2": latte, "3": cappuccino}

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
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        option = input()
        if option == "back":
            return
        coffee = CoffeeMachine.options[option]
        if self.check_amount(coffee=coffee):
            print("I have enough resources, making you a coffee!")
            self.cups -= 1
            self.prepare_coffee(coffee=coffee)
        else:
            print( "Sorry, not enough resources")

    def check_amount(self, coffee):
        if self.cups > 0 and self.water >= coffee.water and \
                self.milk >= coffee.milk and \
                self.coffee_beans >= coffee.coffee_beans:
            return True
        else:
            return False

    def prepare_coffee(self, coffee):
        self.water -= coffee.water
        self.milk -= coffee.milk
        self.coffee_beans -= coffee.coffee_beans
        self.money += coffee.money

    def info(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.coffee_beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money""")


def wrapper(fun):
    print()
    fun()
    print()


if __name__ == "__main__":
    coffee_machine = CoffeeMachine(money=550, water=400, milk=540, coffee_beans=120, cups=9)
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            wrapper(coffee_machine.buy)
        elif action == "take":
            wrapper(coffee_machine.take)
        elif action == "fill":
            wrapper(coffee_machine.fill)
        elif action == "remaining":
            wrapper(coffee_machine.info)
        elif action == "exit":
            break

