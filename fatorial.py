'''
num = float(input("Digite um número: "))
resultado = 1
contador = num

while contador > 1:
    resultado *= contador
    contador -= 1

print("Fatorial de", num, "é", resultado)
'''

def fat(x):
    if x <= 0:
        return 1
    else: return x * fat(x-1)

print(fat(5))