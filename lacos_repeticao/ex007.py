start = int(input("Digite o primeiro número: "))
end = int(input("Digite o segundo número: "))

print('Numeros pares entre {} e {} são:'.format(start,end))

while start <= end:
    if start % 2 == 0:
        print(start)
    start += 1
