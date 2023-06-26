lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = sver3 = mai2 = 0
for v in range(0, 3):
    for h in range(0, 3):
        lst[v][h] = int(input(f'POSIÇÃO [{v}] [{h}]: '))
    print()

print('-' * 30)
for v in range(0, 3):
    for h in range(0, 3):
        print(f'[{lst[v][h]:^3}]', end='')
        if lst[v][h] % 2 == 0:
            spar = spar + lst[v][h]
    print()

for v in range(0, 3):
    sver3 = sver3 + lst[v][2]



print(f' A SOMA DOS VALORES PARES É IGUAL A: {spar}, \n'
      f' A SOMA DOS VALORES DA 3ª LINHA VERTICAL É: {sver3}, \n'
      f' O VALOR MÁXIMO PRESENTE NA SEGUNDA COLUNA HORIZONTAL É: {max(lst[1])}')

