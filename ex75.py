a = int(input('Insira o 1º valor: '))
b = int(input('Insira o 2º valor: '))
c = int(input('Insira o 3º valor: '))
d = int(input('Insira o 4º valor: '))

tpl = (a, b, c, d)

print(tpl)

# a)
if 9 in tpl:
    print(f'O valor 9 aparece {tpl.count(9)} vezes dentro da tupla')
else:
    print('O valor 9 não aparece nenhuma vez dentro da tupla')

# b)
if 3 in tpl:
    print(f'O valor 3 aparece na posição {tpl.index(3)+1}')
else:
    print(f'O valor 3 não aparece nenhuma vez dentro da tupla')

# c)
for n in tpl:
    if n % 2 == 0:
        print(f'Foi digitado o valor par {n}')
