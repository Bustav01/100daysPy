num = 7
primos = [i for i in range(1,num)]
divisores = [d for d in primos if num%d == 0]
for n in divisores:
    print(n)
if len(divisores) == 1 or len(divisores) == 2:
    print('Primo')
else: 
    print('Compuesto')