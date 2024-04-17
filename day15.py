# Coffee Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = resources["money"]
total_money = 0

def checklist(menu, product, water, milk, coffee):
    """_summary_

    Args:
        menu (_type_): _description_
        product (_type_): _description_
        water (_type_): _description_
        milk (_type_): _description_
        coffee (_type_): _description_

    Returns:
        _type_: _description_
    """    
    item = menu[product]
    water_1 = item["ingredients"]["water"]
    milk_1 = item["ingredients"]["milk"]
    coffee_1 = item["ingredients"]["coffee"]
    
    if water >= water_1 and milk >= milk_1 and coffee >= coffee_1:
        return True
    elif water < water_1:
        return "Sorry there is not enough water."
    elif milk < milk_1:
        return "Sorry there is not enough milk."
    elif coffee < coffee_1:
        return "Sorry there is not enough coffee."


def report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")

# Quarter = 25cent, dimes = 10cent, nickel = 5cent, penny = 1cent

print("Welcome to the Coffee Machine ☕.")
print("""Enter your choice:
            1. Espresso - $1.5
            2. Latte - $2.5
            3. Cappuccino - $3.0""")
choice = None

while True:
    choice = input("What is your choice(espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        break
    elif choice == "report":
        report(water=water, milk=milk, coffee=coffee, money=money)
        continue
    
    item = checklist(menu=MENU, product=choice,water=water, milk=milk, coffee=coffee)
    if choice in ["espresso", "latte", "cappuccino"] and item != True:
        print(item)
        continue

    
    quarter = int(input("How many Quarters?: "))*0.25
    dime = int(input("How many Dimes?: "))*0.10
    nickle = int(input("How many Nickles?: "))*0.05
    penny = int(input("How many Pennies?: "))*0.01
    total_money = quarter + dime + nickle + penny
    # print(total_money)

    if choice == "espresso" and total_money >= 1.5:
        water -= 50
        coffee -= 18
        money += 1.5
        print(f"Here is ${round(total_money - 1.5, 2)} in change.")
        print("Here is your espresso ☕️. Enjoy!")
        
    elif choice == "latte" and total_money >= 2.5:
        water -= 200
        milk -= 150
        coffee -= 24
        money += 2.5
        print(f"Here is ${round(total_money - 2.5, 2)} in change.")
        print("Here is your latte ☕️. Enjoy!")   

    elif choice == "cappuccino" and total_money >= 3.0:
        water -= 250
        milk -= 100
        coffee -= 24
        money += 3.0
        print(f"Here is ${round(total_money - 3.0, 2)} in change.")
        print("Here is your cappuccino ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
    
    
