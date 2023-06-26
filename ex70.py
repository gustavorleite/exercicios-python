
print('-' * 30)
lst = []
cont_p = 0
ptotal = 0

while True:

    nome = str(input('PRODUTO: '))
    preco = float(input('PREÇO (EM R$): '))
    if preco > 1000:
        cont_p += 1
    ptotal += preco
    lst += [preco]

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break

menor = min(lst)
print(f'FIM! \nSuas compras deram o total de R${ptotal} \n'
      f'Existem entre os produtos {cont_p} com o valor acima de R$1000,00 \n'
      f'O produto mais barato: R${menor}')