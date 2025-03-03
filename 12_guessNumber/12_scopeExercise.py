def is_prime(num:int)->bool:
    primos = [i for i in range(1,num)]
    divisores = [d for d in primos if num%d == 0]
    divisores.append(num)
    for n in divisores:
        print(n)
    if len(divisores) == 1 or len(divisores) == 2:
        return True
    else: 
        return False

num = 4

print(f'Número {num} es primo?: {is_prime(num)}')