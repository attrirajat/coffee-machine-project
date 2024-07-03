
menu_items = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def ask_money():
    print("We only accept coins.")
    quarter = int(input("Please insert Quarter:") )
    dimes= int(input("Please insert Dimes:"))
    nickles= int(input("Please insert Nickles:"))
    pennies = int(input("Please insert Pennies:"))
    total = (quarter * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total

def process_money(total, choice_option):
    if total >= choice_option:
        change = round(total - choice_option, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += choice_option
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded {total}.")
        return False

def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(coffee_option, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_option} ☕️. Enjoy!")

def print_report():
    print("Generting Report...")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} gm")
    print(f"Money: ${profit}")


is_machine_on = True

while is_machine_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    
    if choice == "off":
        is_machine_on = False
    
    elif choice == "report":
        print_report()
    
    else:
        drink_option = menu_items[choice]
        if check_resources(drink_option["ingredients"]):
            payment = ask_money()

            if process_money(payment, int(drink_option["cost"])):
                make_coffee(choice, drink_option["ingredients"])