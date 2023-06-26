lst = [[], [], []]

for vert in range(0, 3): # 3 NUMEROS DA LINHA VERTICAL [0] [1] [2]
    matriz_0 = int(input(f'POSIÇÃO [{vert}]: '))
    lst[0].append(matriz_0)

print()
for vert in range(0, 3):
    matriz_1 = int(input(f'POSIÇÃO [{vert}]: '))
    lst[1].append(matriz_1)

print()
for vert in range(0, 3):
    matriz_2 = int(input(f'POSIÇÃO [{vert}]: '))
    lst[2].append(matriz_2)

for vert in range(0, 3):
    print(
      f'{lst[0]}\n'
      f'{lst[1]}\n'
      f'{lst[2]}'
)

