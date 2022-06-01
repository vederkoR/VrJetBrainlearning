print("how many ml of water the coffee machine has:")
water_amount = int(input())
print("Write how many ml of milk the coffee machine has:")
milk_amount = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_amount = int(input())
print("Write how many cups of coffee you will need:")
coffee_cups = int(input())
possible_cups = min([int(water_amount / (coffee_cups * 200)), int(milk_amount / (coffee_cups * 50)),
                     int(coffee_amount / (coffee_cups * 15))])
possible_cups_2 = min([int(water_amount / 200), int(milk_amount / 50),
                       int(coffee_amount / 15)])
if possible_cups == 1:
    print("Yes, I can make that amount of coffee")
elif possible_cups == 0:
    print(f"No, I can make only {possible_cups_2} cups of coffee")
else:
    print(f"Yes, I can make that amount of coffee (and even {possible_cups - 1} more than that)")
