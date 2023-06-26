#FUNÇÃO P/ DESCOBRIR MAIOR VALOR
from time import sleep

lst = []

def maior(* num):
    cont = maior = 0
    for v in num:
        sleep(0.3)
        print(f'{v} ', end='')
        lst.append(v)

        mv = max(lst)

        ml = len(lst)

    print(f'\nForam informados {ml} valores'
          f'\nO maior valor na lista indicada é: {mv}')
    lst.clear()
    print('-' * 50)

#pp
maior(2, 3, 4, 5, 6, 3, 3, 12, 11, 10)
maior(82, 8239, 83294, 8448, 223, 00, 1)
