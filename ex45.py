    # PEDRA PAPEL E TESOURA
import random
from time import sleep
import emojia

print(''' 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

emoticon = ([emoji.emojize(':victory_hand:'), emoji.emojize(':raised_hand:'), emoji.emojize(':raised_fist:')])

sleep(0.5)
print('{:^40}'.format('JO'))
sleep(0.5)
print('{:^41}'.format('KEN'))
sleep(0.5)
print('{:^43}'.format('PO!!'))
jogador = int(input('{:^20}'.format(' ')))

                    # JOGADOR

if jogador == 0:
    print('Joagor: Pedra', (emoticon[2]))

elif jogador == 1:
    print('Jogador: Papel', (emoticon[1]))

elif jogador == 2:
    print('Jogador: Tesoura', (emoticon[0]))

                    # COMPUTADOR
lista = [0, 1, 2]
computador = random.choice(lista)

if computador == 0: # pedra
    print('Computador: Pedra', (emoticon[2]))
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')

elif computador == 1: # papel
    print('Computador: Papel', (emoticon[1]))
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')

elif computador == 2: # tesoura
    print('Computador: Tesoura', (emoticon[0]))
    if jogador == 0:
        print('JGOADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')