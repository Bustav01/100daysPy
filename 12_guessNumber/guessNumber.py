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
import time
from 12_art.py import *

numero:int = random.randint(1,100)
