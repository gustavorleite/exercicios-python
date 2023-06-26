soma = 0
cont = 0
for numeros_inteiros in range(1, 7):
    numeros = int(input(f'Valor {numeros_inteiros}: '))
    if numeros % 2 == 0:
        soma = soma + numeros
        cont = cont + 1
        print(f'A soma dos valores PARES indicados é: {soma} ')
    else:
        print()