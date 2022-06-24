const input = require('sync-input')

class Coffee {
    constructor(water = 0, milk = 0, coffee_beans = 0, money = 0) {
        this.water = water;
        this.milk = milk;
        this.coffee_beans = coffee_beans;
        this.money = money;
    }
}

class CoffeeMachine {


    constructor(water, milk, coffee_beans, cups, money) {
        this.water = water;
        this.milk = milk;
        this.coffee_beans = coffee_beans;
        this.money = money;
        this.cups = cups;
        this.espresso = new Coffee(250, 0, 16, 4);
        this.latte = new Coffee(350, 75, 20, 7);
        this.cappuccino = new Coffee(200, 100, 12, 6)
        this.options = {"1": this.espresso, "2": this.latte, "3": this.cappuccino};
    }

    take() {
        console.log(`I gave you $${this.money}`);
        this.money = 0;
    }

    fill() {
        console.log("Write how many ml of water you want to add:");
        this.water += Number(input());
        console.log("Write how many ml of milk you want to add:");
        this.milk += Number(input());
        console.log("Write how many grams of coffee beans you want to add:");
        this.coffee_beans += Number(input());
        console.log("Write how many disposable cups you want to add:");
        this.cups += Number(input());
    }

    check_amount(coffee) {
        return this.cups > 0 && this.water >= coffee.water &&
            this.milk >= coffee.milk &&
            this.coffee_beans >= coffee.coffee_beans;
    }

    prepare_coffee(coffee) {
        this.water -= coffee.water;
        this.milk -= coffee.milk;
        this.coffee_beans -= coffee.coffee_beans;
        this.money += coffee.money;
    }

    buy() {
        console.log("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:");
        let option = input();
        if (option === "back") {
            return
        }
        let coffee = this.options[option];
        if (this.check_amount(coffee)) {
            console.log("I have enough resources, making you a coffee!");
            this.cups -= 1;
            this.prepare_coffee(coffee);
        } else {
            console.log("Sorry, not enough resources");
        }
    }

    info() {
        console.log(`The coffee machine has:
${this.water} ml of water
${this.milk} ml of milk
${this.coffee_beans} g of coffee beans
${this.cups} disposable cups
$${this.money} of money`)
    }
}


let coffee_machine = new CoffeeMachine(400, 540, 120, 9, 550)
console.log()
while (true) {
    console.log("Write action (buy, fill, take, remaining, exit):")
    let action = input()
    console.log()
    if (action === "buy") {
        coffee_machine.buy()
    } else if (action === "take") {
        coffee_machine.take()
    } else if (action === "fill") {
        coffee_machine.fill()
    } else if (action === "remaining") {
        coffee_machine.info()
    } else if (action === "exit") {
        break
    }
    console.log()
}