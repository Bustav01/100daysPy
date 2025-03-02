import random

def get_carta() -> dict:
    cartas = {'A':11,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    pintas = ['♠','♣','♥','♦']
    c = list(random.choice(list(cartas.items())))
    p = random.choice(pintas)

    return {'Carta':c[0],
            'Numero':c[1],
            'Pinta':p}

def sum_carta(cartas:list) -> int:
    out = 0
    for c in cartas:
        if c['Carta'] == 'A' and (out + c['Numero']) > 21:
            out += 1
        else:
            out += c['Numero']
    return out

def mk_carta(c:dict) -> dict:
    top = ' ___ '
    if len(c['Carta']) == 1:
        p1 = f'|{c['Carta']}  |'
    else:
        p1 = f'|{c['Carta']} |'
    mid = f'| {c['Pinta']} |'
    if len(c['Carta']) == 1:
        p2 = f'|__{c['Carta']}|'
    else:
        p2 = f'|_{c['Carta']}|'
    
    return {'top':top,
            'p1':p1,
            'mid':mid,
            'p2':p2}

def start(qty:int=2) -> list:
    c = [get_carta() for i in range(qty)]
    return c


def merge_cartas(cartas:list[dict]) -> dict[list]:
    '''Une la lista de cartas para aplicar formato visible'''
      
    secciones_cartas = {'head':[],
           'arriba':[],
           'medio':[],
           'abajo':[]}
    
    for carta in cartas:
        secciones_cartas['head'].append(carta['top'])
        secciones_cartas['arriba'].append(carta['p1'])
        secciones_cartas['medio'].append(carta['mid'])
        secciones_cartas['abajo'].append(carta['p2'])
    #print(secciones_cartas) 

    for seccion in secciones_cartas:
        secciones_cartas[seccion] = ' '.join(secciones_cartas[seccion])
    #print(secciones_cartas)
    return secciones_cartas

def vis_cartas(player_c) -> None:
    '''Aplica formato a cartas para ser mostradas cuando sea necesario'''
    vis_cartas = merge_cartas([mk_carta(c) for c in player_c])
    print(f'{vis_cartas['head']}\n{vis_cartas['arriba']}\n{vis_cartas['medio']}\n{vis_cartas['abajo']}\n')

def chk_cartas(usr_c:list[dict],dlr_c:list[dict], u_sum:int, d_sum:int) -> None:
    '''Muestra el modelo de cartas para ambos jugadores según formato para fin de juego.'''
    print('Tus cartas:')
    vis_cartas(usr_c)
    print(f'Suma de tus cartas: {u_sum}')
    print('Cartas del dealer:')
    vis_cartas(dlr_c)
    print(f'Suma dealer: {d_sum}')

def seguir_jugando() -> str:
    respuestas = ['si','no']
    while True:
        try:
            r = input('¿Desea seguir jugando? Escribe: "si" o "no". ').lower()
            if r in respuestas:
                return r
            else:
                raise Exception
        except:
            print('Debes escribir "si" o "no"')

def dlr_play(cartas) -> str:
    '''Dealer desea sacar más cartas?'''
    if sum_carta(cartas) >= 17: return 'no'
    else: return 'si'

def chk_ganador(usr_c:list[dict], dlr_c:list[dict]) ->bool:
    '''Confirma quien gana.
    '''
   
    usr_puntaje = sum_carta(usr_c)
    dlr_puntaje = sum_carta(dlr_c)

    if usr_puntaje > 21 and dlr_puntaje > 21:
        chk_cartas(usr_c, dlr_c, usr_puntaje, dlr_puntaje)
        print('Todos pierden')
    elif usr_puntaje > 21:
        chk_cartas(usr_c, dlr_c, usr_puntaje, dlr_puntaje)
        print('Perdiste :c')
    elif dlr_puntaje > 21:
        chk_cartas(usr_c, dlr_c, usr_puntaje, dlr_puntaje)
        print('Ganaste c:')
    else:
        # Caso en el que ninguno se pasa de 21
        chk_cartas(usr_c, dlr_c, usr_puntaje, dlr_puntaje)
        if usr_puntaje > dlr_puntaje:
            print('Ganaste c:')
        elif usr_puntaje < dlr_puntaje:
            print('Perdiste :c')
        else:
            print('Empate')
    



