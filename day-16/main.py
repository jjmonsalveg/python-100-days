from enum import Enum

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


class MachineOptions(Enum):
    CAPPUCCINO = "cappuccino"
    ESPRESSO = "espresso"
    LATTE = "latte"
    OFF = "off"
    REPORT = "report"


def coffee_machine() -> None:
    on = True
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()

    while on:
        try:
            choice = MachineOptions(
                input(f"What would you like? ({menu.get_items()})").casefold()
            )

            match choice:
                case (
                    MachineOptions.LATTE
                    | MachineOptions.CAPPUCCINO
                    | MachineOptions.ESPRESSO
                ):
                    menu_item = menu.find_drink(choice.value)
                    enough_resources = coffee_maker.is_resource_sufficient(menu_item)

                    if not enough_resources:
                        continue

                    enough_money = money_machine.make_payment(menu_item.cost)

                    if not enough_money:
                        continue

                    coffee_maker.make_coffee(menu_item)

                case MachineOptions.OFF:
                    on = False
                case MachineOptions.REPORT:
                    coffee_maker.report()
                    money_machine.report()
        except ValueError as e:
            print(e)


coffee_machine()
