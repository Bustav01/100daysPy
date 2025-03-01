'''
TODO: subasta anónima
bienvenida
preguntar nombre
preguntar monto
hay más compradores?
limpiar pantalla
repetir hasta que alguien diga no.

mostrar nombre y monto de quien dio más
'''
import os




logo = r'''
               ___________
               \         /
                )_______(
                |"""""""|_.-._,.---------.,_.-._
                |       | | |               | | ''-.
                |       |_| |_             _| |_..-'
                |_______| '-' `'---------'` '-'
                )"""""""(
               /_________\
               `'-------'`
             .-------------.
            /_______________\
'''

ofertantes = {} # Nombre:monto
continuar = True
while continuar == True:
    print(logo + '\nBienvenido a la subasta de Los IFV de la caballería blindada')
    nombre:str = input("¿Cuál es su nombre?: ").lower()
    monto:int = int(input("¿Cuál es su oferta? $"))
    ofertantes[nombre] = monto
    
    p_continuar = input('¿Alguien más desea ofertar?\nEscriba "si" o "no". ').lower()
    if p_continuar == "no":
        continuar = False
    elif p_continuar == 'si':
        os.system('cls')

#print(ofertantes)

#qué pasa si dos ofertan lo mismo?: el primero en hacerlo gana
res = max(ofertantes, key=ofertantes.get) #Obtiene la key
print(f'¡Felicitaciones, el ganador es {res}, con una oferta de ${ofertantes[res]}')