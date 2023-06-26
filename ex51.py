    # PROGRESSAO ARITMÉTICA
soma = 0
cont = 0
print('{:^40}'.format(' 10 PRIMEIROS TERMOS DE UMA PROGRESSÃO ARITMÉTICA '))

termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo = termo + (10-1) * razao
for c in range (termo, decimo, razao):
    print(f'{c}', end=' > ')
    continue
print('FIM')