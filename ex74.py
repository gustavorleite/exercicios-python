# TUPLAS ALEATORIAS

from random import randint

a1 = randint(1, 10)
a2 = randint(1, 10)
a3 = randint(1, 10)
a4 = randint(1, 10)
a5 = randint(1, 10)

aleatorio = (a1, a2, a3, a4, a5)
print(f'{aleatorio}\n'
      f'{sorted(aleatorio)}') # TUPLA ORDENADA - (MENOR P/ MAIOR)