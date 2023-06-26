
lst = []
lst_par = []
lst_impar = []

for v in range(1, 7+1):
    value = int(input(f'Digite o {v}ª valor: '))
    lst.append(value)
    if value % 2 == 0:
        lst_par.append(value)
    else:
        lst_impar.append(value)

lst.sort()
lst_par.sort()
lst_impar.sort()

print(f'LISTA COMPLETA: {lst}, \n'
      f'LISTA (PARES): {lst_par}, \n'
      f'LISTA (IMPARES): {lst_impar}')
