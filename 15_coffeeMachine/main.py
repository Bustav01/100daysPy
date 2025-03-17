'''
TODO: Recursos no parece estar validando correctamente
'''
import os
from methods_15  import *

def main():
    recursos:dict[str, int] = {
    'cafe': 100,
    'agua': 1000,
    'leche': 500,
    'dinero': 0 #TODO: convertir a diccionario de monedas
    }
    menu = [k for k in sabores]
    pedido = get_input('¿Qué sabor deseas?', menu, recursos)
    #os.system('cls')
    monedas = {
            500:0,
            100:0,
            50:0,
            10:0,
            }
    if pedido == 'recharge':
        print('Recargando')
        recursos['cafe'] = 100
        recursos['agua'] = 1000
        recursos['leche'] = 500
        time.sleep(5)
        print('Recarga exitosa')
        return recursos
    elif pedido in menu:
        print(f'Pedido: {pedido}, Precio: ${sabores[pedido]['costo']}')
        #pedir monedas
        monedas = get_coin(monedas)

        #hacer café
        hacerCafe = mk_coffee(sabores[pedido],monedas, recursos)
        if hacerCafe == False:
            return None
        else:
            print(f'DEBUG: pedido: {sabores[pedido]}')
            rUses = sabores[pedido]['ingredientes'] #ValueError: too many values to unpack (expected 2)
            rUses['costo'] = chk_coin(monedas, sabores[pedido]['costo'])
            recursos = update_resources(recursos, rUses)

if __name__ == "__main__":
    while True:
        main()