from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()

    menu_items = menu.get_items()
    serve = True
    #Loop pedido:
    while serve == True:
        request = input(f"Menú: {menu_items}\n")
        order = menu.find_drink(request)
        print(request)
        if request == None:
            serve == False #Cortar loop
        elif request == 'report':
            coffee.report()
            money.report()
        else:
            bill = order.cost
            serve = money.make_payment(bill)
if __name__ == "__main__":
    main()