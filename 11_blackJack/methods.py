import random

def get_carta()->dict:
    cartas = {'A':11,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
    pintas = ['♠','♣','♥','♦']
    c = list(random.choice(list(cartas.items())))
    p = random.choice(pintas)

    return {'Carta':c[0],
            'Numero':c[1],
            'Pinta':p}

def sum_carta(cartas:list)->int:
    out = 0
    for c in cartas:
        if c['Carta'] == 'A' and (out + c['Numero']) > 21:
            out += 1
        else:
            out += c['Numero']
    return out

def mk_carta(c:dict):
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

def start()->list:
    return [get_carta(),get_carta()]


def merge_cartas(cartas:list[dict])->dict:
      
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

def seguir_jugando():
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

def chk_win(usr_c,dlr_c):
    
    
    pass
    
def dlr_play(cartas):
    '''Desea sacar más cartas?'''
    if sum_carta >= 17: return 'no'
    else: return 'si'

