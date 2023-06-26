from random import randint
from time import sleep

lst = []
jogos = []

cartelas = int(input('Quantas cartelas serão preenchidas?  '))

for p in range(0, cartelas):
    for c in range(0, 6):
        num = randint(1, 60)
        n_ms = print(f'{num:^3}', end='  ') # PRECISAVA-SE CORRIGIR A PROBABILIDADE DE SAIR ALEATORIAMENTE O MESMO NUMERO EM UMA DAS LISTAS COMPOSTAS
        sleep(0.2)
        lst.append(num)
        if len(lst) >= 6:
            jogos.append(lst[:])
            lst.clear()
    print()

print(f'Seus jogos são: {jogos}')