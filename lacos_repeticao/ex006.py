import random
num_aleatorio = random.randint(1,10)
num_chutado = None
while num_chutado != num_aleatorio:
    num_chutado = int(input('Digite o numero: '))
    if num_chutado > num_aleatorio:
        print('Chutou alto')
    elif num_chutado < num_aleatorio:
        print('Chutou baixo')
    else:
        print('Acertou o numero!')
print("Operação encerrada")