lst = []
lst_par = []
lst_impar = []

while True:
    n = int(input('Digite um valor: '))
    lst.append(n)
    if n % 2 == 0:
        lst_par.append(n)
    else:
        lst_impar.append(n)

    c = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if c in 'Ss':
        continue
    elif c in 'Nn':
        break
    else:
        print('Invalido.')
        input()

print(f'LISTA = {lst.sort()}',
      f'\nPARES = {lst_par.sort()}',
      f'\nIMPARES = {lst_impar.sort()}')