'''
TODO: Recursos no parece estar validando correctamente
'''

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
            rUses = {k:-v for (k,v) in sabores[pedido]['ingredientes']}
            rUses['dinero'] = chk_coin(monedas, sabores[pedido]['costo'])
            recursos = {k: v + rUses[k] for (k,v) in recursos if rUses[k] != None}

if __name__ == "__main__":
    while True:
        main()