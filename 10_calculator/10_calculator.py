'''
TODO:
pedir número, 
pedir operación  +-*/
pedir otro número
mostrar cálculo y resultado.
    escribir s para continuar calculando, tomando como primer número al resultado.
        repetir
    escribir n para empezar un nuevo cálculo
        limpiar pantalla
'''
import re

def suma(n1,n2):
    return n1+n2

def resta(n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

def limpiar_op(txt:str):
    ops_dict = {"*":multiplicar,"/":dividir,"+":suma,"-":resta,}
    op_order:list = [['*','/'],['+','-']]
    op_str:str = ''.join(sum(op_order, []))
    
    #Dividir según numeros u operación
    tx_limpio:list = re.split(f'([{re.escape(op_str)}])', txt)
    #Convertir números a número
    tx_limpio = [int(e) for e in tx_limpio if e not in op_order]

    tmp_res:list = []
    for o in op_order:
        i = 0
        for i, e in enumerate(tx_limpio):
            if e in o:
                n1 = tx_limpio.pop(i -1)
                n2 = tx_limpio.pop(i + 1)
                res = ops_dict[o](n1, n2)
                del tx_limpio[i]
                tx_limpio.insert(i - 1, res)

    return tx_limpio

def ejecutar():
    pass



entrada:str = input("Escribe la wea:\n")