import random
a1 = str(input('nome do aluno 1: '))
a2 = str(input('nome do aluno 2: '))
a3 = str(input('nome do aluno 3: '))
a4 = str(input('nome do aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('a ordem será: {} '.format (lista))
