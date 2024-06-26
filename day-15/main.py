from enum import Enum

MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

format = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

money = 0
class MachineOptions(Enum):
    CAPPUCCINO = "cappuccino"
    ESPRESSO = "espresso"
    LATTE = "latte"
    OFF = "off"
    REPORT = "report"



def print_resources():
    for resource, quantity in resources.items():
        print(f"{resource.title()}: {quantity}{format[resource]}")

    print(f"Money : ${money}")

def insert_coins() -> float:
    print("Please insert coins.")

    total = int(input(("How many quarters?:"))) * 0.25
    total += int(input(("How many dimes?:"))) * 0.10
    total += int(input(("How many nickles?:"))) * 0.05
    total += int(input(("How many pennies?:"))) * 0.01

    return total

def check_resources(product_menu: dict) -> bool:
    enough_resources = True

    for ingredient in product_menu["ingredients"]:
        if product_menu["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough_resources = False

    return enough_resources

def check_amount(total_coins:float, product_menu: dict) -> bool:
    product_cost = product_menu["cost"]

    if total_coins >= product_cost:
        change = round(total_coins - product_cost, 2)

        if change > 0:
            print(f"Here is ${change} dollars in change.")

        global money 
        money += product_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffe(choice: MachineOptions) -> None:
    product_menu = MENU[choice.value]

    for ingredient in product_menu["ingredients"]:
        resources[ingredient] -= product_menu["ingredients"][ingredient]

    print(f"Here is your { choice.value }. Enjoy!")

def coffe_machine() -> None:
    on = True

    while on:
        try:
            choice = MachineOptions(input("What would you like? (espresso/latte/cappuccino)").casefold())

            match choice:
                case MachineOptions.LATTE |  MachineOptions.CAPPUCCINO | MachineOptions.ESPRESSO:
                    product_menu = MENU[choice.value]
                    enough_resources = check_resources(product_menu)

                    if not enough_resources:
                        continue

                    total_coins = insert_coins()
                    enough_money = check_amount(total_coins, product_menu)

                    if not enough_money:
                        continue
                    make_coffe(choice)

                case MachineOptions.OFF:
                    on = False
                case MachineOptions.REPORT:
                    print_resources() 
        except ValueError as e:
            print(e)


coffe_machine()


# DONE
# TODO: if resources aren't enough, print a message “Sorry there is not enough water.”
# TODO: ask the user what they want to drink "What would you like? (espresso/latte/cappuccino):”"
# TODO: Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: When the user enters “report” to the prompt, a report should be generated that shows the current resource values
# TODO: ask the user to insert coins
# TODO: check if the user has inserted enough money to purchase the drink they selected
# TODO: if resources aren't enough "Sorry that's not enough money. Money refunded."
# TODO: check if the resources are enough and make the coffee
# TODO: if resources excced requirements, print a message “Here is $2.45 dollars in change.”
# TODO: once the transaction is successful, update the resources and print a message “Here is your latte. Enjoy!”


# for name, quantity in product["ingredients"].items():
#     if ingredients[item] >
