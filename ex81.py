lst = []

while True:
    lst.append(int(input('Digite um valor p/ inserir: ')))
    q = str(input('Deseja continuar [S/N]: ')).upper().strip()
    if q in 'Ss':
        continue
    elif q in 'Nn':
        break
    else:
        print('Invalido!')

print(lst)
print(f'Você digitou ao todo {len(lst)} elemento(s)')
lst.sort(reverse=True)
print(f'Os elementos dispostos em ordem decrescente são: {lst} ')