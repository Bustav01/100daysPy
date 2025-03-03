'''
TO DO: bienvenida, mision es encontrar tesoro
izquierda o derecha: derecha fin
nadar o esperar: nadar fin
cual puerta? rojo y azul fin
amarillo ganar
'''


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


print("¡Bienvenido/a a la isla del tesoro!\nTu misión es encontrar el tesoro.")

cruce:str = input('Te encuentras en un cruce, ¿Qué dirección eliges?\n      Escribe "izquierda" o "derecha"\n').lower()
if cruce == "derecha":
    print("Moriste :c")
    exit()
isla:str = input('Te encuentras en una isla, ¿vas a esperar que pase un bote o vas a nadar?\n      Escribe "nadar" o "esperar"').lower()
if isla == "nadar":
    print("Moriste :c")
    exit()
puerta:str = input('Encuentras tres puertas: una azul, una roja, una amarilla. ¿Cuál deseas cruzar?\n      Escribe "azul","roja" o "amarilla"').lower()
if puerta == "azul" or puerta == "roja":
    print("Moriste :c")
    exit()
print("ganaste c:")