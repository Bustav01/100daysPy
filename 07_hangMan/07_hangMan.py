'''
TO DO: jugar al colgado.
'''
import random

def get_palabra(lista):
    return random.choice(lista)
def get_indices(c,cadena):
    indices = [i for i, letra in enumerate(cadena) if letra == c]
    return indices
def update_pregunta(pregunta, palabra, letra):
    indices = get_indices(letra, palabra)
    for i in indices:
        pregunta[i] = letra
    return pregunta   


#Generar palabra random:
palabras = ['ALFOMBRA','AMALGAMA','RODODENDRO','EFIMERO','HIPOPOTOMONSTROSESQUIPEDALOFOBIA',
            'ULTERIOR','INFRAVALORADO','QUALIA','SOBREESDRUJULA','EXTENSO','DIFICIL',
            'VINAGRE','HOJALATA',"CASA", "PERRO", "GATO", "ARBOL", "CIELO", "MAR", "MONTAÑA", "CIUDAD", "RÍO", "LUNA",
    "SOL", "FUEGO", "VIENTO", "TIERRA", "NUBE", "ESTRELLA", "FLOR", "CAMINO", "CIEGA", "HOMBRE",
    "LIBRO", "PUERTA", "MESA", "SILLA", "CARRO", "CAMINO", "MANO", "LAPIZ", "CABALLO", "ESCOLA",
    "HOSPITAL", "PARQUE", "CUADRO", "PLATO", "FAMILIA", "AMIGO", "TIENDA", "VENTANA", "CUERPO", "ROPA"]

colgado = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']



palabra = get_palabra(palabras)
#print(f'DEBUG: {palabra}')

#Generar _ por cada letra:
pregunta = []
for c in palabra:
    pregunta.append('_')
# print(pregunta)


#Iniciar juego

'''
mientras palabra no completa:
    pedir letra
        es correcto o no?
            si letra ya usada:
            si correcto: reemplazar _ por letra según índices encontrados en lista.

                si palabra completa: ganar
            si falso: quitar una vida, dibujar barra.
                si vidas = 0, fallar.

'''
intentos = 6
letras_usadas = []
print("Una persona morirá por tu culpa si no adivinas la palabra :)")
while True:
    es_correcto = False
    print(colgado[intentos])
    print(f"Palabra: {''.join(pregunta)}\n{len(pregunta)} letras")
    letra = input(f"Tienes {intentos} intentos.\nEscribe una letra:\n").upper()
    if letra in palabra:
        if letra in letras_usadas:
            intentos -= 1
            print(f"Ya usaste esta letra :c")
        else:
            letras_usadas.append(letra)
            pregunta = update_pregunta(pregunta, palabra, letra)
    else:
        intentos -= 1
        print("La palabra no tiene esta letra :c")

        
    
    if intentos == 0:
        print(colgado[intentos])
        print(f"Perdiste :c\n¡La palabra era {palabra}!")
        exit()
    if '_' not in pregunta:
        print("Ganaste c:")
        exit()