import time
from data import *

def get_report(r:dict) -> None:
    print(f'Agua: {r['agua']}ml\nCafé: {r['cafe']}g')
    print(f'Leche: {r['leche']}ml\nDinero: ${r['dinero']}')

def get_coin(m):
    '''Ingresar cantidades por moneda'''
    while True:
        try:
            entrada = input()
            pass
        except ValueError:
            pass

def get_input(string:str, opt:list[str], r:dict) -> str|None:
    while True:
        try:
            entrada = input(f'{string} Escribe {r"/".join(opt)} ').lower()
            if entrada == 'report':
                get_report(r)
            elif entrada == 'off':
                time.sleep(1)
                print('Apagando...')
                time.sleep(2)
                exit()
            elif entrada in opt or entrada == 'recharge':
                return entrada
            else:
                raise ValueError
        except ValueError:
            print(f'ERROR: Entrada no válida. Debe escribir una de las siguientes opciones:\n{r"/".join(opt)}')

def chk_resources(pedido:dict, r:dict) -> bool :
    '''Confirma que la máquina tiene los recursos suficientes'''
    out = [r[k] >= pedido[k] for k in pedido]    #Confirma que máquina tiene más material que solicitado, sino Falso en indx
    [print(f'No hay suficiente: {k}') for k in pedido if r[k] < pedido[k]]  #Imprime fallos

    if False in out:
        return False
    else:
        return True

def chk_coin(coins:dict, cost:int) -> int:
    '''Confirma que las monedas ingresadas suman la cantidad suficiente
    Retorna Pago - Costo'''
    suma = sum([k*coins[k] for k in coins])
    return (suma - cost)

def chk_payment(coins: dict, pedido:dict, r:dict) -> bool:
    '''Confirma que los materiales son suficientes y el pago es correcto. Devuelve dinero si sobra'''
    
    hayMaterial = [chk_resources(pedido['ingredientes'], r)]
    pago = chk_coin(coins, pedido['costo'])
    if pago >= 0:
        print(f'Monto insuficiente\n...se devolverá el dinero.')
    elif pago == 0:
        print(f'Monto pagado')
    else:
        print(f'Monto pagado. Saldo a devolver: {pago}')
    
    if hayMaterial == True and pago >= 0:
        return True
    else:
        return False

def mk_coffee(pedido:dict, coins:dict, r:dict):
    '''Imprime preparación de café si se confirma pago y materiales disponibles. Modifica recursos en máquina'''
    esValido:bool = chk_payment(coins,pedido,r)

    if esValido == True:
        print('Preparando café')
        for k in pedido['ingredientes']:
            print(f'Agregando {k.title()}...')
            time.sleep(2)
            print('Listo.')
        return True
    else:
        return False
