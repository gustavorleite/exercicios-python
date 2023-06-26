# P.A
print('Gerador de Progressão Aritmetica (PA)')
print('- ' * 20)
p_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

pa = p_termo
cont = 1

while cont <= 10:
    print(f'{pa}', end='')
    if cont < 10:
        print(' >>> ', end='')
    else:
        print('\nFIM', end='')
    cont += 1
    pa += razao