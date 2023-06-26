from random import randint
from operator import itemgetter

dict = {}

for j in range(1, 4+1):
    dados = randint(1, 6)
    dict[f'JOGADOR{j}'] = dados
    print(f'JOGADOR {j} tirou: {dados} pontos')

print()

ordem = print(sorted(dict.values()))
# noinspection NonAsciiCharacters
posição = max(dict.values())
print(f'O MAIOR VALOR FOI {posição}.')
vencedor = sorted(dict.items(), key=itemgetter(1), reverse=True)
print()

#opcional
for i, v in enumerate(vencedor):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')
