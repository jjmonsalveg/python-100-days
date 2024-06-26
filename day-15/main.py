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


