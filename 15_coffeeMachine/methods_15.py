import time
import re
from data import *

def get_report(r:dict) -> None:
    print(f'Agua: {r['agua']}ml\nCafé: {r['cafe']}g')
    print(f'Leche: {r['leche']}ml\nDinero: ${r['dinero']}')

def get_coin(m:dict) -> dict:
    '''Ingresar cantidades por moneda'''
    segmento = r'\d+'                           # Detecta número de cualquier dígito
    patron = r','.join([segmento for k in m])   # Añade segmentos por cada llave en diccionario de monedas (m)
    formato = r",".join(f'{k}' for k in m)      # 0,0,0... según diccionario

    while True:
        try:
            #Solicitar cantidad de monedas según estructura de diccionario:
            entrada = input(f'Ingrese la cantidad para cada moneda\nFormato: {formato} ')
            if re.match(patron, entrada):
                #Convertir entrada a lista, valores a número, obtener índice y asignar valores a diccionario:
                return {k: int(entrada.split(',')[i]) for i,k in enumerate(m)}
            else:
                raise ValueError
        except ValueError:
            print(f'''ERROR: debe ingresar cantidad de monedas según formato: {formato}
                  Los valores mostrados son los tipos de moneda según casilla''')

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
    print(f'DEBUG: sumando monedas {suma}')
    return (suma - cost)

def chk_payment(coins: dict, pedido:dict, r:dict) -> bool:
    '''Confirma que los materiales son suficientes y el pago es correcto. Devuelve dinero si sobra'''
    print(f'DEBUG: Chequeando pago:')
    hayMaterial = chk_resources(pedido['ingredientes'], r)

    print(f'DEBUG: hay material: {hayMaterial}')
    pago = chk_coin(coins, pedido['costo'])
    print(f'DEBUG: pago: {pago}')
    if pago < 0:
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
