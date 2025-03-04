'''
TODO: logo, 
mostrar dos personas al azar (A,B)
escribe A o B (quién tiene más seguidores?)
validar respuesta (correcto, incorrecto.)
'''
import random
import os
from art_14 import *
from sujetos import datos

def pick_subjects() -> list:
    return random.choice(datos, 2) #Error

def set_answer(subjects:list) -> str :
    if subjects[0]['cantidad_comparar'] == subjects[1]['cantidad_comparar']:
        return 'IGUALES'
    elif subjects[0]['cantidad_comparar'] < subjects[1]['cantidad_comparar']:
        return 'B'
    elif subjects[0]['cantidad_comparar'] > subjects[1]['cantidad_comparar']:
        return 'A'
    
def show_subject(subject, r) -> None:
    '''TODO: En un futuro, podría añadir una dificultad, que muestre sólo algunos campos'''
    print(f'OPCIÓN {r}')
    print(f'Recurso: {subject['nombre']}\nTipo: {subject['descripcion']}\nPaís: {subject['pais']}')

def player_input(string:str, entries:list):
    while True:
        try:
            entrada = input(string).upper()
            if entrada not in entries:
                raise ValueError
            else:
                return entrada
        except ValueError:
            print(f'Debe escribir una de las opciones: {entries}')



correctas = 0
incorrectas = 0
seguir_jugando = True
while seguir_jugando == True:
    print('hola')
    sujetos = pick_subjects()
    correcta_respuesta:str = set_answer(sujetos)
    print('Qué recurso tiene mayor producción en sus países?')
    show_subject(sujetos[0],'A')
    print('VS')
    show_subject(sujetos[1],'B')

    jugador_respuesta:str = player_input('Escribe A, B o "Iguales"', ['A','B','IGUALES'])
    if jugador_respuesta == correcta_respuesta:
        correctas += 1
        print('Correcto! c:')
    else:
        incorrectas += 1
        print('Incorrecto :c')
    jugar_de_nuevo = player_input('¿Desea seguir jugando?', ['SI','NO'])
    if jugar_de_nuevo == 'SI':
        os.system('cls')
    else:
        os.system('cls')
        print(f'Respuestas correctas: {correctas}\nRespuestas Erróneas: {incorrectas}')

    



