'''
TODO: jugar blackjack
sacar dos cartas al azar
    preguntar por 1 más
        si 1 más, sacar 1 carta
    sumar cartas
    comparar con 21
'''
import os
from methods import *



# cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10] #si 11 y sobre 21: 1

logo = r'''
___.   .__                 __          __               __     ________ _______  _______  _______   
\_ |__ |  | _____    ____ |  | __     |__|____    ____ |  | __ \_____  \\   _  \ \   _  \ \   _  \  
 | __ \|  | \__  \ _/ ___\|  |/ /     |  \__  \ _/ ___\|  |/ /   _(__  </  /_\  \/  /_\  \/  /_\  \ 
 | \_\ \  |__/ __ \\  \___|    <      |  |/ __ \\  \___|    <   /       \  \_/   \  \_/   \  \_/   \
 |___  /____(____  /\___  >__|_ \ /\__|  (____  /\___  >__|_ \ /______  /\_____  /\_____  /\_____  /
     \/          \/     \/     \/ \______|    \/     \/     \/        \/       \/       \/       \/ 
'''

usuario_cartas:list[dict] = []
dealer_cartas:list[dict] = []
es_inicio:bool = True
keep_playing:bool = True
while keep_playing == True:
    print(logo)
    if es_inicio == True: 
        usuario_cartas = start()
        dealer_cartas = start()
    vis_usr_cartas = merge_cartas([mk_carta(c) for c in usuario_cartas])
    vis_dlr_cartas = merge_cartas([mk_carta(c) for c in dealer_cartas])
    suma_cartas_usr = sum_carta(usuario_cartas)
    suma_cartas_dlr = sum_carta(dealer_cartas)

    print('Tus cartas:')
    print(f'{vis_usr_cartas['head']}\n{vis_usr_cartas['arriba']}\n{vis_usr_cartas['medio']}\n{vis_usr_cartas['abajo']}\n')
    print(f'Suma de tus cartas: {suma_cartas_usr}')
    if suma_cartas_usr > 21:
            keep_playing = False
            print('Perdiste :c')
            exit()
    usr_jugar = seguir_jugando()
    dlr_jugar = dlr_play(dealer_cartas)
    if dlr_jugar == 'no':
         print(f'Cartas del Dealer:\n{vis_dlr_cartas}')

    if usr_jugar == 'no':
        keep_playing = False
    else:
        usuario_cartas.append(get_carta())
        if suma_cartas_usr > 21:
            keep_playing = False
            print('Perdiste :c')
        else:
            es_inicio = False
            os.system('cls')




# os.system('cls')



