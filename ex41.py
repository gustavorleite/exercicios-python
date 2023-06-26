    # ANALISANDO TRIANGULOS V.2
print('-' *6)
A = int(input('Lado 1: '))
B = int(input('Lado 2: '))
C = int(input('Lado 3: '))

if A < B + C and B < A + C and C < A + B:
    print('TRIANGULO', end='')
    if A == B == C:
        print(' EQUILATERO')
    elif A != B != C and A != C != B:
        print(' ESCALENO')
    else:
        print(' ISOSCELES')

else:
    print('ERROR! Os nº indicados não podem formar uma triangulo')