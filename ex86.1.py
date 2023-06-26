lst = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for v in range(0, 3):
    for h in range(0, 3):
        lst[v][h] = int(input(f'POSIÇÃO V[{v}], H[{h}]: '))
print()
for v in range(0, 3):
    for h in range (0, 3):
        print(f'[{lst[v][h]}]', end='')
    print()
