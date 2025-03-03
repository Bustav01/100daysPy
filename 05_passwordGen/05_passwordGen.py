'''
TO DO: password generator:
cuantas letras?
cuantos símbolos?
cuántos números?
print lista
print password
'''
import random as rd

letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!','-','_'] #'$','%','&','(',')','*','+']


nLetras:int = int(input("¿Cuántas letras quiere en su contraseña?\n"))
nNumeros:int = int(input("¿Cuántos números quiere en su Password?\n"))
nSimbolos:int = int(input("¿Cuántos símbolos quiere en su Password?\n"))


lista = [letras, numeros, simbolos]
tipoChar = [nLetras, nNumeros, nSimbolos]


tmpPass = []
count = 0
for c in tipoChar:
    for i in range(tipoChar[count]):
        tmpPass.append(rd.choice(lista[count]))
    count += 1

#print(''.join(tmpPass))
password = []

#TO DO: Reordenar
rd.shuffle(tmpPass)
print(''.join(tmpPass))


