'''
TO DO: cachipun
'''

import random as rd

piedra:str = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
PIEDRA
"""

papel:str = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
PAPEL
"""

tijera:str = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
TIJERA
"""

manos:list = [piedra, papel, tijera, piedra]


jugada:int = int(input('Elige:\n  0 - Piedra\n  1 - Papel\n  2 - Tijera\n'))
if jugada not in [0,1,2]:
    print("Debes elegir 0, 1 o 2")
    exit()

print(f"Tu jugada:\n{manos[jugada]}")

pc:str = rd.randint(0,2)
print(f"Jugada de la máquina:\n{manos[pc]}")

if pc == jugada:
    print("Empate")
elif manos[jugada] == manos[pc + 1]:
    print("Ganaste")
else:
    print("Perdiste :c")
    
exit()