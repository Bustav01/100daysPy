'''
TODO: cifrado cesar
dirección: escribe encode para encriptar, decode para desencriptar
texto: escribir el mensaje
cambio: cuantas letras debe cambiar

'''

def encrypt(txt:str, chg:int, alfabeto:list)->str:
    out = ''
    for l in txt:
        if l not in alfabeto:
            pass
        else:
            i = alfabeto.index(l) + chg
            i %= len(alfabeto)
            out += alfabeto[i]
    return out

def decrypt(txt:str, chg:int, alfabeto:list)->str:
    out = ''
    for l in txt:
        i = alfabeto.index(l) - chg
        i %= len(alfabeto)
        out += alfabeto[i]
    return out

def caesar(txt:str, chg:int, alfabeto:list, op:str )->str:
    out = ''
    if op == 'decode':
        chg *= -1
    for l in txt:
        if l not in alfabeto:
            out += l
        else:
            i = alfabeto.index(l) + chg
            i %= len(alfabeto)
            out += alfabeto[i]
    return out

alfabeto = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direccion = input('Qué operación desea realizar?\nEscriba "encode" para encriptar\nEscriba "decode" para desencriptar\n').lower()
texto = input("Cuál es el mensaje?\n").lower()
cambio = int(input("Cuál es el valor de cifrado?\n"))

out = caesar(texto, cambio, alfabeto, direccion)

print(out)