    #
n = 0
s = 0
soma = 0

while n != 999:
    n = int(input('Digite o nº desejado (999 p/ parar): '))
    if n == 999:
        break

    s += 1
    soma += n

print(f'O nº de valores escritos foi {s}')
print(f'A soma dos valores escritos foi {soma}')
