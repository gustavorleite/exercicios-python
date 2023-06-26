
def contador(i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}')

    if f > i:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            cont = cont + p     # cont += p
    elif i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont = cont - p     # cont -= p

    if p < 0:
        p = p * (-1)

    print('FIM')

# programa principal

# a)
contador(1, 10, 1)

# b)
contador(10, 0, 2)

# c)
painel = print('CONTAGEM PERSONALIZADA')
print('-' * 25)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo/Intervalo: '))
contador(inicio, fim, passo)