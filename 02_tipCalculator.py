'''
TO DO: Tip Calculator
Bienvenida
cuál es el precio? $(input)
qué porcentaje te gustaría dar? 10, 12, o 15? (input)
en cuántas personas se va a dividir?(input)
Cada persona debería pagar: ($res.ultado)
'''

print("Bienvenido/a a la calculadora de propinas!")
precio:float = float(input("¿Cuánto es el precio a pagar? $"))
propina:float = int(input("¿Qué porcentaje de propina te gustaría dar? ¿10, 12 o 15?"))/100 + 1
personas:int = int(input("¿Cuántas personas van a pagar?: "))

resultado:float = round((precio * propina)/personas)
print(f"Cada persona debería pagar: ${resultado:.2f}")
