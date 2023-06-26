lst = []
for cont in range(0, 5):
    lst.append(int(input('Insira o valor: ')))

for p, q in enumerate(lst):
    print(f'Na posição {p} encontrei o valor {q}')

posicao_max = lst.index(max(lst))
posicao_min = lst.index(min(lst))
print(f'O maior valor na lista foi {max(lst)} na posição {posicao_max} ')
print(f'O menor valor na lista foi {min(lst)} na posição {posicao_min}')
