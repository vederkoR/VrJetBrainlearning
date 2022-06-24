const input = require('sync-input')

class CoffeeMachine {
    constructor(water, milk, coffee_beans, cups, money) {
        this.water = water;
        this.milk = milk
        this.coffee_beans = coffee_beans
        this.money = money
        this.cups = cups
    }

    take() {
        console.log(`I gave you ${this.money}`)
        this.money = 0
    }

    fill() {
        console.log("Write how many ml of water you want to add:")
        this.water += Number(input())
        console.log("Write how many ml of milk you want to add:")
        this.milk += Number(input())
        console.log("Write how many grams of coffee beans you want to add:")
        this.coffee_beans += Number(input())
        console.log("Write how many disposable cups you want to add:")
        this.cups += Number(input())
    }

    buy() {
        this.cups -= 1
        console.log("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:");
        let option = Number(input())
        if (option === 1) {
            this.water -= 250
            this.coffee_beans -= 16
            this.money += 4
        } else if (option === 2) {
            this.water -= 350
            this.milk -= 75
            this.coffee_beans -= 20
            this.money += 7
        } else if (option === 3) {
            this.water -= 200
            this.milk -= 100
            this.coffee_beans -= 12
            this.money += 6
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
coffee_machine.info()
console.log()
console.log("Write action (buy, fill, take):")
action = input()
if (action === "buy") {
    coffee_machine.buy()
} else if (action === "take") {
    coffee_machine.take()
} else if (action === "fill") {
    coffee_machine.fill()
}
console.log()
coffee_machine.info()
