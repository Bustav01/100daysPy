# TODO: añadir recarga

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()

    menu_items = menu.get_items()
    is_on = True
    #Loop pedido:
    while is_on == True:
        request = input(f"Menú: {menu_items}\n")
        if request == 'off':
            is_on = False
        elif request == 'report':
            coffee.report()
            money.report()
        else:
            order = menu.find_drink(request)
            if coffee.is_resource_sufficient(order) == True:
                if money.make_payment(order.cost) == True:
                    coffee.make_coffee(order)
if __name__ == "__main__":
    main()