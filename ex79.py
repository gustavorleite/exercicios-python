print('Adicione quantos nº deseja em sua lista. Para finalizar digite N')

lst = []

while True:
    valor = (int(input('Insira o valor desejado: ')))

    if valor not in lst:
        lst.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado...')
        lst.append(valor)
        lst.pop()   # Meio burro mas apaga o append acima, ou seja, "não adiciona" o valor repetido

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'S':
        continue
    if continuar == 'N':
        break
    else:
        continuar2 = str(input('Invalido. Deseja continuar? [S/N] ')).strip().upper()
        if continuar2 == 'S':
            continue
        if continuar2 == 'N':
            break
        else:
            print('Invalido. Finalizando ...')

print('-' * 30, '\n'
    f'{sorted(lst)}')
