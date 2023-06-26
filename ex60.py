# FATORIAL
from math import factorial

f = int(input('Escolha um nº para verificar sua fatorial: '))

fat = f
while fat >= 1:
    print(f'{fat} x 'if fat > 1 else '1 = ', end='')
    fat = fat -1
print(factorial(f))





