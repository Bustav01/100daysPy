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
        order = input(f"Menú: {menu_items}\n")
        print(order)
        if menu.find_drink(order) == None:
            serve == False #Cortar loop
        elif order == 'report':
            coffee.report()
            money.report()
        else:
            order 
            bill = input(money.make_payment()) #Continuar proceso


    





if __name__ == "__main__":
    main()