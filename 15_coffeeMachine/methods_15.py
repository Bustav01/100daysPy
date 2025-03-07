import time
from data import *

def get_report() -> None:
    print(f'Agua: {recursos['agua']}ml\nCafé: {recursos['cafe']}g')
    print(f'Leche: {recursos['leche']}ml\nDinero: ${recursos['dinero']}')

def get_input(string:str, opt:list[str]) -> str|None:
    while True:
        try:
            entrada = input(f'{string} Escribe {r"/".join(opt)} ').lower()
            if entrada == 'report':
                get_report()
                return
            elif entrada == 'off':
                time.sleep(1)
                print('Apagando...')
                time.sleep(2)
                exit()
            elif entrada == 'recharge':
                '''
                recursos['agua'] = 1000
                recursos['cafe'] = 100
                recursos['leche'] = 500
                '''
                return entrada
            elif entrada in opt:
                return entrada
            else:
                raise ValueError
        except ValueError:
            print(f'ERROR: Entrada no válida. Debe escribir una de las siguientes opciones:\n{r"/".join(opt)}')

def chk_resources(pedido:dict) -> bool :
    '''Confirma que la máquina tiene los recursos suficientes'''
    pass

def chk_coin(coins, cost:int) -> bool:
    '''Confirma que las monedas ingresadas suman la cantidad suficiente'''
    pass

def chk_payment() -> bool:
    '''Confirma que los materiales son suficientes y el pago es correcto. Devuelve dinero si sobra'''
    pass

def mk_coffee():
    '''Imprime preparación de café si se confirma pago y materiales disponibles. Modifica recursos en máquina'''
    pass

