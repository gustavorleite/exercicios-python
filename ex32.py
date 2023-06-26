import math
print(' O Ano Bissexto consiste no ano que tem 366 dias, ou seja, um dia a mais do que os 365 habituais.\n Esse "dia extra" ocorre a cada 4 anos, quando é adicionado o 29 de fevereiro no calendário.')
print('_' * 50)
a = int(input(' '
              'Insira um ano e verifique se ele é, ou não, um ano bissexto: '))
if a % 4 == 0 and a != 0 or a % 400 == 0:
    print(' O ano é BISSEXTO')
else:
    print(' O ano NÃO é BISSEXTO')
