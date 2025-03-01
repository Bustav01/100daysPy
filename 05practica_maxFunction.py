'''
TO DO: hacer función max con for loop, listas y condiciones.

num puede ser igual que siguiente
num puede ser mayor que siguiente
num puede ser menor que siguiente

'''


numeros = [12, 45, 78, 134, 256, 99, 201, 65, 87, 310, 
           145, 230, 72, 55, 410, 198, 890, 329, 84, 250, 67, 500]

numMax = 0
for num in numeros:
    if num > numMax:
        numMax = num

print(numMax)