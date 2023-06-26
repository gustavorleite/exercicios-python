numero = int(input('Digite um nº: '))
tot = 0
for c in range(1, numero+1):
    # print(f'{c} ', end='')
    if numero % c == 0:
        print('\033[31m', end='')
        tot = tot + 1
    else:
        print('\033[m', end='')
if tot == 2:
    print('\nO nº é PRIMO')
else:
    print('\nO nº não é PRIMO')
