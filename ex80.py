lst = list()    # ou lst = []
for p in range (0, 5):
    valor = int(input('Digite um valor: '))
    if p == 0 or valor > lst[(len(lst)-1)]: # lst[-1]       # PRIMEIRO E ULTIMO VALOR = POS(0) E MAX(VALOR)
        lst.append(valor)
    else:
        pos = 0
        while pos < len(lst):
            if valor <= lst[pos]:
                lst.insert(pos, valor)
                break
            p += 1
print(lst)