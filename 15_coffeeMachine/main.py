from methods_15  import *

recursos:dict[str, int] = {
    'cafe': 100,
    'agua': 1000,
    'leche': 500,
    'dinero': 0 #TODO: convertir a diccionario de monedas
    }

def second(r) -> dict|None:
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
        r['cafe'] = 100
        r['agua'] = 1000
        r['leche'] = 500
        time.sleep(5)
        print('Recarga exitosa')
        return r
    elif pedido in menu:
        #pedir monedas
        tmpMonedas = get_coin(monedas)
        monedas = {k: v + tmpMonedas[k] for (k,v) in monedas}
        #hacer café
        hacerCafe = mk_coffee(sabores[pedido],monedas, r)
        if hacerCafe == False:
            return None
        else:
            out = {k:-v for (k,v) in sabores[pedido]['ingredientes']}
            out['dinero'] = chk_coin(monedas, 0)
            return out #Devuelve negativo para gasto y dinero
            

def main():
    recursos:dict[str, int] = {
    'cafe': 100,
    'agua': 1000,
    'leche': 500,
    'dinero': 0 #TODO: convertir a diccionario de monedas
    }

    while True:
        tmp = second(recursos)
        if tmp != None:
            recursos = {k: v + tmp[k] for (k,v) in recursos if tmp[k] != None}

if __name__ == "__main__":
    main()