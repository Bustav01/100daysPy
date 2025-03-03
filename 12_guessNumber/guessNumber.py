'''
TODO:Bienvenida,
elegir número entre 1 y 100
elegir dificultad
mostrar intentos
LOOP:
    haz un intento
    si incorrecto:
        feedback (muy alto, muy bajo)
    si correcto:
        ganaste.
    tienes N intentos
'''

import random
import os
from art_12 import *


def get_level(r:list[str]) -> str:
    lvl:str = ''
    #print(f'DEBUG: Valor R: {r}\nTipo R: {type(r)}')
    while lvl not in r:
        lvl:str = input('Elige la dificultad, facil o dificil: ').lower()
        #print(f'DEBUG: lvl: {lvl}')
        if lvl not in r:
            print(f'Debes escribir "{r[0]}" o "{r[1]}"')
        else:
            return lvl

def get_play()->int:
    while True:
        try:
            j:int = int(input('Adivina el número: '))
            if 1 <= j <= 100:
                return j
            else:
                print('Debes ingresar un número entre 1 y 100')
        except ValueError:
            print('Debes ingresar un número')

def validate_play(n:int,p:int) -> int:
    if p != n:
        # imprimir demasiado alto o bajo
        if p > n:
            print('Incorrecto, tu número es muy alto')
        elif p < n:
            print('Incorrecto, tu número es muy bajo')
        return False
    else:
        print('¡Correcto! c:')
        return True

def jugar():
    numero:int = random.randint(1,100)
    #print(f'DEBUG: número: {numero}')
    D_NIVELES = {'facil':10,'dificil':5}
    nivel = get_level(list(D_NIVELES.keys()))
    intentos:int = D_NIVELES[nivel]

    #LOOP
    while intentos != 0:
        print(f'Tienes {intentos} intentos.')
        jugada:int = get_play()
        resultado = validate_play(numero, jugada)
        if resultado == False:
            intentos -= 1
        else:
            break

def play_again():
    respuesta = ['si','no']
    while True:
        try:
            r = input('¿Desea jugar de nuevo?. Responda "si" o "no" ').lower()
            if r not in respuesta:
                raise ValueError
            else:
                return r
        except ValueError:
            print('Debe escribir "si" o "no"')

seguir_jugando:bool = True
while seguir_jugando == True:
    iniciar()
    jugar()
    pregunta = play_again()
    if pregunta == 'no':
        seguir_jugando = False
        os.system('cls')

    
