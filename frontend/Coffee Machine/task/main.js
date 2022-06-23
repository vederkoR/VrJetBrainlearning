// Use "input()" to input a line from the user
// Use "input(str)" to print some text before requesting input
// You will need this in the following stages
const input = require('sync-input')

console.log("how many ml of water the coffee machine has:")
let water_amount = Number(input())
console.log("Write how many ml of milk the coffee machine has:")
let milk_amount = Number(input())
console.log("Write how many grams of coffee beans the coffee machine has:")
let coffee_amount = Number(input())
console.log("Write how many cups of coffee you will need:")
let coffee_cups = Number(input())
let possible_cups = Math.min(Math.floor(water_amount / (coffee_cups * 200)), Math.floor(milk_amount / (coffee_cups * 50)),
    Math.floor(coffee_amount / (coffee_cups * 15)))
let possible_cups_2 = Math.min(Math.floor(water_amount / 200), Math.floor(milk_amount / 50),
    Math.floor(coffee_amount / 15))
if (possible_cups === 1) {
    console.log("Yes, I can make that amount of coffee")
}
else if (possible_cups === 0) {
    console.log(`No, I can make only ${possible_cups_2} cups of coffee`)
} else {
    console.log(`Yes, I can make that amount of coffee (and even ${possible_cups - 1} more than that)`)
}
