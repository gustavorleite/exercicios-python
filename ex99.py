from random import randint

lst = list()

for c in range(0, 9):
    lst.append(randint(1, 10))

def maior():
    print('-'* 100)
    print(f'Foram escolhidos aleatoriamente os valores: {lst}')
    print(f'O maior valor dentre os citados foi: {max(lst)}')
    print('-'* 100)

#pp
maior()