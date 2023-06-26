# funçao sortear e somar

from random import randint
from time import sleep

def sorteia(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)

def somaPar(lista):
    lst_par = []
    pares = 0
    for v in lista:
        if v % 2 == 0:
            pares += v

    print(f'Somando os valores pares em {lista} temos: {(pares)}')
    print()


nums = list()
#pp
sorteia(nums)
print()
somaPar(nums)

